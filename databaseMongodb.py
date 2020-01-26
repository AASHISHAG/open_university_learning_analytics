# connect to mongoDB and process the data

# import
from pymongo import MongoClient

# defining database class
class Database():
    def __init__(self):
        client = MongoClient("mongodb+srv://database_student:qwert67890@cluster0-y3wgg.mongodb.net/test?retryWrites=true&w=majority")
        #client = MongoClient("mongodb://localhost:27017")
        db = client.get_database('mydb')
        self.coll = db.trends

    def insertStudent(self,prediction,value1=99, value2=99, value3=99, value4=99, value5=99, value6=99, value7=99, value8=99, value9=99, value10=99, value11=99):
        return self.coll.insert_one({"gender": value1, "region": value2,"highest_education": value3,"imd_band": value4,
                              "age_band": value5,"num_of_prev_attempts": value6,
                              "is_banked": value7,"code_module_x": value8,"code_presentation_x": value9,
                              "code_module_y": value10,"code_presentation_y": value11,"prediction":prediction})

    def findAll(self):
        return self.coll.find()

    def find(self, variable, value):
        return self.coll.find({variable: value})

    def gender(self):
        try:
            male =  self.coll.find({"gender": 1}).count()
            female = self.coll.find({"gender": 0}).count()
        except:
            male=0
            female=0
        return male,female

    def prediction(self):
        try:
            w_male   =  self.coll.find({"gender": 1, "prediction": "Withdrawn"}).count()
            w_female =  self.coll.find({"gender": 0, "prediction": "Withdrawn"}).count()

            p_male   =  self.coll.find({"gender": 1, "prediction": "Pass"}).count()
            p_female =  self.coll.find({"gender": 0, "prediction": "Pass"}).count()

            f_male   =  self.coll.find({"gender": 1, "prediction": "Fail"}).count()
            f_female =  self.coll.find({"gender": 0, "prediction": "Fail"}).count()

            d_male   =  self.coll.find({"gender": 1, "prediction": "Distinction"}).count()
            d_female =  self.coll.find({"gender": 0, "prediction": "Distinction"}).count()

        except:
            w_male=0
            w_female=0
            p_male=0
            p_female=0
            f_male=0
            f_female=0
            d_male=0
            d_female=0

        return w_male,w_female,p_male,p_female,f_male,f_female,d_male,d_female

    # return the number of document in the DB
    def num_of(self, variable, value):
        return self.coll.find({variable: value}).count()

    # return the dataset size
    def db_size(self):
        return self.coll.find().count()

    # return one document
    def findOne(self, variable, value):
        return self.coll.find_one({variable: value})

    # update one document
    def updateOne(self, variable, value, update):
        self.coll.update_one({variable: value}, {'$set': update})

    # delete one document
    def deleteOne(self, variable, value):
        self.coll.delete_one({variable: value})
