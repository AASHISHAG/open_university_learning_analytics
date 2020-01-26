#main file to run the server and render the html templates

# imports
import json
import numpy as np
from prediction import predict
from labelEncoder import encode
from traverseJson import read_json
from werkzeug.utils import redirect
from database_mongodb import Database
from flask import Flask, render_template, request, url_for

db = Database()

# app configuration
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

# input fields
student_information = [
    "gender",
    "region",
    "highest_education",
    "imd_band",
    "age_band",
    "num_of_prev_attempts",
    "is_banked",
    "code_module_x",
    "code_presentation_x",
    "code_module_y",
    "code_presentation_y"]

student_information_decoded = [
    "gender",
    "region",
    "highest_education",
    "imd_band",
    "age_band",
    "num_of_prev_attempts",
    "is_banked",
    "code_module_x",
    "code_presentation_x",
    "code_module_y",
    "code_presentation_y"]

# route for handling the home page
@app.route('/')
@app.route('/home')
def main():
    return render_template('index.html')

# route for handling the dataset page
@app.route('/dataset')
def dataset():
    return render_template('dataset.html', title='Dataset')

# route for handling the machine learning page
@app.route('/machinelearning')
def machinelearning():
    return render_template('machinelearning.html', title='Machine Learning')


# route for handling the questionnaire page
@app.route('/questionForm', methods=['GET', 'POST'])
def dataForm():
    error = None

    gender = ['Select Gender',
              'Female',
              'Male']

    region = ['Select Region',
              'East Anglian Region',
              'East Midlands Region',
              'London Region',
              'North Region',
              'North Western Region',
              'Scotland',
              'South Region',
              'South East Region',
              'West Midlands Region',
              'Wales',
              'Yorkshire Region']

    highest_education = ['Select Highest Education',
                         'No Formal Qualification',
                         'Lower Than A Level',
                         'A Level or Equivalent',
                         'Higher Education Qualification',
                         'Post Graduation Qualification']

    imd_band = ['Select IMD Band',
                '0-10%',
                '10-20%',
                '20-30%',
                '30-40%',
                '40-50%',
                '50-60%',
                '60-70%',
                '70-80%',
                '80-90%',
                '90-100%'
                ]

    age_band = ['Select Age Group',
                '0-35',
                '35-55',
                '55<=']

    num_of_prev_attempts = ['Select Number Of Previous Attempts',
                            0,
                            1,
                            2,
                            3,
                            4,
                            5,
                            6]

    is_banked = ['Select Semester',
                 0,
                 1]

    code_module_x = ['Select First Module',
                     'AAA',
                     'BBB',
                     'CCC',
                     'DDD',
                     'EEE',
                     'FFF',
                     'GGG']

    code_presentation_x = ['Select Semester (First Module)',
                           '2013B',
                           '2013J',
                           '2014B',
                           '2014J']

    code_module_y = ['Select Second Module',
                     'AAA',
                     'BBB',
                     'CCC',
                     'DDD',
                     'EEE',
                     'FFF',
                     'GGG']

    code_presentation_y = ['Select Semester (Module Second)',
                           '2013B',
                           '2013J',
                           '2014B',
                           '2014J']

    if request.method == 'POST':
        '''if request.form['gender'] == 'Select Gender' or request.form['region'] == 'Select Region' \
                or request.form['highest_education'] == 'Select Highest Education' \
                or request.form['imd_band'] == 'Select IMD Band' \
                or request.form['age_band'] == 'Select Age Group' \
                or request.form['num_of_prev_attempts'] == 'Select Number Of Previous Attempts' \
                or request.form['is_banked'] == 'Select' \
                or request.form['code_module_x'] == 'Select First Module' \
                or request.form['code_presentation_x'] == 'Select First Semester (First Module)' \
                or request.form['code_module_y'] == 'Select Second Module' \
                or request.form['code_presentation_y'] == 'Select Semester (Second Module)':
            error = 'Select all fields'
        else:'''
        student_information_decoded[0] = request.form['gender']
        Gender = student_information[0] = encode(request.form['gender'])
        student_information_decoded[1] = request.form['region']
        Region = student_information[1] = encode(request.form['region'])
        student_information_decoded[2] = request.form['highest_education']
        HighestEducation = student_information[2] = encode(request.form['highest_education'])
        student_information_decoded[3] = request.form['imd_band']
        IMDBand = student_information[3] = encode(request.form['imd_band'])
        student_information_decoded[4] = request.form['age_band']
        AgeGroup = student_information[4] = encode(request.form['age_band'])
        student_information_decoded[5] = request.form['num_of_prev_attempts']
        NumberOfPreviousAttempts = student_information[5] = encode(request.form['num_of_prev_attempts'])
        student_information_decoded[6] = request.form['is_banked']
        Semester = student_information[6] = encode(request.form['is_banked'])
        student_information_decoded[7] = request.form['code_module_x']
        FirstModule = student_information[7] = encode(request.form['code_module_x'])
        student_information_decoded[8] = request.form['code_presentation_x']
        SemesterFirstModule = student_information[8] = encode(request.form['code_presentation_x'])
        student_information_decoded[9] = request.form['code_module_y']
        SecondModule = student_information[9] = encode(request.form['code_module_y'])
        student_information_decoded[10] = request.form['code_presentation_y']
        SemesterSecondModule = student_information[10] = encode(request.form['code_presentation_y'])
        print(student_information)
        return redirect(url_for('prediction'))
    return render_template('question_form.html', error=error, gender=gender, region=region,
                           highest_education=highest_education, imd_band=imd_band, age_band=age_band,
                           num_of_prev_attempts=num_of_prev_attempts, is_banked=is_banked, code_module_x=code_module_x,
                           code_presentation_x=code_presentation_x, code_module_y=code_module_y, code_presentation_y=code_presentation_y,
                           title='Questionaire')

# route for handling prediction page
@app.route('/prediction')
def prediction():
    print("Student details: {}".format(student_information))
    # student = np.array(student_information)
    # pred_result = predict('decision-tree', student_information)
    pred_result, accuracy = predict(student_information)
    print("Prediction: {}".format(pred_result))
    try:
        print(db.insertStudent(pred_result,student_information[0], student_information[1], student_information[2], student_information[3],
                         student_information[4], student_information[5], student_information[6], student_information[7],
                         student_information[8], student_information[9], student_information[10]))
    except:
        print("Fail to save the student data to DB.")

    accuracy = round(accuracy * 100, 2)
    print("Accuracy: {}".format(accuracy))

    if (None in student_information):
        path = '0 of f, 0 of i, 7 of n, 627 of a'
    else:
        path = read_json(student_information[0], student_information[1], student_information[2], student_information[3],
                    student_information[4], student_information[5], student_information[6],
                    student_information[7], student_information[8], student_information[9], student_information[10])

    student_information_decoded_no_select = [x if 'Select' not in x else None for x in student_information_decoded]

    value_1 = 'None' if 'None' in str(student_information[0]) else str(student_information_decoded_no_select[0]) +" (" + str(student_information[0]) + ")"
    value_2 = 'None' if 'None' in str(student_information[1]) else str(student_information_decoded_no_select[1]) + " (" + str(student_information[1]) + ")"
    value_3 = 'None' if 'None' in str(student_information[2]) else str(student_information_decoded_no_select[2]) + " (" + str(student_information[2]) + ")"
    value_4 = 'None' if 'None' in str(student_information[3]) else str(student_information_decoded_no_select[3]) + " (" + str(student_information[3]) + ")"
    value_5 = 'None' if 'None' in str(student_information[4]) else str(student_information_decoded_no_select[4]) + " (" + str(student_information[4]) + ")"
    value_6 = 'None' if 'None' in str(student_information[5]) else str(student_information_decoded_no_select[5]) + " (" + str(student_information[5]) + ")"
    value_7 = 'None' if 'None' in str(student_information[6]) else str(student_information_decoded_no_select[6]) + " (" + str(student_information[6]) + ")"
    value_8 = 'None' if 'None' in str(student_information[7]) else str(student_information_decoded_no_select[7]) + " (" + str(student_information[7]) + ")"
    value_9 = 'None' if 'None' in str(student_information[8]) else str(student_information_decoded_no_select[8]) + " (" + str(student_information[8]) + ")"
    value_10 = 'None' if 'None' in str(student_information[9]) else str(student_information_decoded_no_select[9]) + " (" + str(student_information[9]) + ")"
    value_11 = 'None' if 'None' in str(student_information[10]) else str(student_information_decoded_no_select[10]) + " (" + str(student_information[10]) + ")"

    return render_template('prediction.html', feature_1 = 'Gender', value_1 = value_1,
                           feature_2='Region', value_2 = value_2,
                           feature_3='Highest Education', value_3 = value_3,
                           feature_4='IMD Band', value_4 = value_4,
                           feature_5='Age Group', value_5 = value_5,
                           feature_6='Number Of Previous Attempts', value_6 = value_6,
                           feature_7='Semester', value_7 = value_7,
                           feature_8='First Module', value_8 = value_8,
                           feature_9='Semester (First Module)', value_9 = value_9,
                           feature_10='Second Module', value_10 = value_10,
                           feature_11='Semester (Second Module)', value_11 = value_11,
                           student=accuracy, pred_result=pred_result, path=path, title='Prediction')

# route for handling the aboutus page
@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')

# route for handling the decision tree visualisation page
@app.route('/tree')
def tree():
    with open('rules.json') as json_file:
        data = json.load(json_file)
    return render_template('tree2.html', data=data, title="Tree")

# route for handling the rules page (test page for reference)
@app.route('/rules')
def rules():
    return render_template('rules.json')

# route for handling the website analytics page
@app.route('/trends')
def trends():
    male, female = db.gender()
    w_male, w_female, p_male, p_female, f_male, f_female, d_male, d_female = db.prediction()
    return render_template('trends.html',
                           male=male, female=female, w_male=w_male, w_female=w_female,
                           p_male=p_male, p_female=p_female, f_male=f_male, f_female=f_female,
                           d_male=d_male, d_female=d_female, title='Trends')

# main function
if __name__ == "__main__":
    app.run()
