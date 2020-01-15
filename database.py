from pymongo import *


class Database:
    def __init__(self, collection='labels'):
        client = MongoClient()
        self.db = client.webNutritionDB[collection]

    def insert_result(self, url, result):
        self.db.insert_one({"url": url, "result": result})

    def upsert_result(self, url, label, ldict):
        self.db.update_one({"url": url}, {"$set": {
            label: ldict
        }}, True)

    def find_result(self, url):
        return self.db.find_one({"url": url})

    def count_result(self, column_name, name_of_instance):
        return self.db.aggregate([{'$match': {column_name: {'$eq': name_of_instance}}}, {'$count': name_of_instance}])

    def find_unique_count_result(self, column_name):
        return self.db.aggregate([{'$match': {column_name: {'$not': {'$size': 0}}}}, {'$unwind': '$' + column_name},
                                  {'$group': {'_id': {'$toLower': '$' + column_name}, 'y': {'$sum': 1}}},
                                  {'$match': {'y': {'$gte': 1}}}, {'$sort': {'y': -1}}, {'$limit': 6}])
