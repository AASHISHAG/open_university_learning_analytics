from pymongo import MongoClient


class Database():
    def __init__(self):
        client = MongoClient(
            "mongodb+srv://database_student:qwert67890@cluster0-y3wgg.mongodb.net/test?retryWrites=true&w=majority")
        db = client.get_database('mydb')
        self.coll = db.test  # rename test with oula after testing

    def insertStudent(self, newStudentData):
        self.coll.insert_one(newStudentData)

    def findAll(self):
        return self.coll.find()

    def findOne(self, variable, value):
        return self.coll.find_one({variable: value})
