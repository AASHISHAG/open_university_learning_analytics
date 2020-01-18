from pymongo import MongoClient


class Database():
    def __init__(self):
        client = MongoClient(
            "mongodb+srv://database_student:qwert67890@cluster0-y3wgg.mongodb.net/test?retryWrites=true&w=majority")
        db = client.get_database('mydb')
        self.coll = db.test

    def insertStudent(self, newStudentData):
        self.coll.insert_one(newStudentData)

    def findAll(self):
        return self.coll.find()

    def findOne(self, variable, value):
        return self.coll.find_one({variable: value})

    def updateOne(self, variable, value, update):
        self.coll.update_one({variable: value}, {'$set': update})

    def deleteOne(self, variable, value):
        self.coll.delete_one({variable: value})
