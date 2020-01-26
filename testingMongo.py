#testing the connection to MongoDB

# import libraries
import pprint
from databaseMongodb import Database

db = Database()

# Insert one sample data to db
""" student_data = {
    "is_banked": "0",
    "code_module_x": "BBB",
    "code_presentation_x": "2015J",
    "gender": "F",
    "region": "West Anglian Region",
    "highest_education": "Ab",
    "imd_band": "90-100%",
    "age_band": "35-55",
    "num_of_prev_attempts": "0",
    "final_result": "Withdrawn",
    "code_module_y": "CCC",
    "code_presentation_y": "2014C"
} """

# Insert student data
""" db.insertStudent(student_data) """

# find all entries in database and prints
""" for post in db.findAll():
    pprint.pprint(post) """

# find one entry in database
""" pprint.pprint(db.findOne('code_module_y', 'CCC')) """

# update one entry in database
""" student_update = {"is_banked": "1"}
db.updateOne('code_module_y', 'BBB', student_update)
pprint.pprint(db.findOne('code_module_y', 'BBB')) """

# delete one entry in database
""" db.deleteOne('code_module_x', 'AAA')
pprint.pprint(db.findOne('code_module_x', 'AAA')) """