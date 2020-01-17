import plot as plt
from prediction import predict
import numpy as np
from labelEncoder import encode
from werkzeug.utils import redirect
from flask import Flask, render_template, flash, request, url_for
#from Model_classification import predictFunction, validation_data

# app configuration
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

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

# route for handling the login page logic
@app.route('/')
@app.route('/home')
def main():
    return render_template('index.html')

# route for handling the prediction page logic
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
                         'A Level or Equivalent',
                         'Lower Than A Level',
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
        if request.form['gender'] == 'Select Gender' or request.form['region'] == 'Select Region'\
                or request.form['highest_education'] == 'Select Highest Education'\
                or request.form['imd_band'] == 'Select IMD Band' \
                or request.form['age_band'] == 'Select Age Group'\
                or request.form['num_of_prev_attempts'] == 'Select Number Of Previous Attempts'\
                or request.form['is_banked'] == 'Select'\
                or request.form['code_module_x'] == 'Select First Module'\
                or request.form['code_presentation_x'] == 'Select First Semester (First Module)'\
                or request.form['code_module_y'] == 'Select Second Module'\
                or request.form['code_presentation_y'] == 'Select Semester (Second Module)':
                error = 'Select all fields'
        else:
            print(request.form['gender'])
            student_information[0] = encode(request.form['gender'])
            student_information[1] = encode(request.form['region'])
            student_information[2] = encode(request.form['highest_education'])
            student_information[3] = encode(request.form['imd_band'])
            student_information[4] = encode(request.form['age_band'])
            student_information[5] = encode(request.form['num_of_prev_attempts'])
            student_information[6] = encode(request.form['is_banked'])
            student_information[7] = encode(request.form['code_module_x'])
            student_information[8] = encode(request.form['code_presentation_x'])
            student_information[9] = encode(request.form['code_module_y'])
            student_information[10] = encode(request.form['code_presentation_y'])
            print(student_information)
            return redirect(url_for('prediction'))
    return render_template('question_form.html', error = error, gender = gender, region = region, highest_education = highest_education,
                           imd_band = imd_band, age_band = age_band, num_of_prev_attempts = num_of_prev_attempts,
                           is_banked = is_banked, code_module_x = code_module_x, code_presentation_x = code_presentation_x,
                           code_module_y = code_module_y, code_presentation_y = code_presentation_y, title='Questionaire')
@app.route('/prediction')
def prediction():
    print(student_information)
    student = np.array(student_information)
    #studentTwoDArray = np.reshape(student, (-1, 16))
    pred_result = predict(student_information)
    print(pred_result)
    # plot data
    #mean_female_grade = plt.mean_female_grade
    #mean_male_grade = plt.mean_male_grade
    #mean_fifteen_year = plt.mean_fifteen_year
    #mean_sixteen_year = plt.mean_sixteen_year
    #mean_seventeen_year = plt.mean_eighteen_year
    #mean_eighteen_year = plt.mean_eighteen_year
    #mean_nineteen_year = plt.mean_nineteen_year
    #mean_twenty_year = plt.mean_twenty_year

    return render_template('prediction.html',mean_twenty_year=10,
                           mean_nineteen_year=10,mean_eighteen_year=10
                           ,mean_seventeen_year=10,mean_sixteen_year=10,
                           mean_fifteen_year=10,mean_female_grade=10,
                           mean_male_grade = 10 ,student=student, pred_result=10, title='Prediction')

    #return render_template('prediction.html', title='Prediction')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

if __name__ == "__main__":
    app.run()