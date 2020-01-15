import plot as plt
import numpy as np
from Convertor import *
from werkzeug.utils import redirect
from flask import Flask, render_template, flash, request, url_for
from Model_classification import predictFunction, validation_data


# app configuration
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

studentInformation = [
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
def main():
    return render_template('index.html')

# route for handling the prediction page logic
@app.route('/questionForm', methods=['GET', 'POST'])
def dataForm():
    error = None

    gender = ['Select Gender',
              'Female', 'Male']

    region = ['Select Region',
              'East Anglian Region', 'East Midlands Region',
              'London Region',
              'North Region', 'North Western Region',
              'Scotland', 'South Region', 'South East Region',
              'West Midlands Region', 'Wales',
              'Yorkshire Region']

    highest_education = ['Select Highest Education', 'No Formal Qualification',
                         'A Level or Equivalent', 'Lower Than A Level',
                         'HE Qualification', 'Post Graduate Qualification']

    imd_band = ['Select IMD Band',
                '0-10%', '10%-20%', '20%-30%',
                '30%-40%', '40%-50%', '50%-60%'
                '60%-70%', '70%-80%' '80%-90%', '90%-100%'
                 ]

    age_band = ['Select Age Group',
                '0-35', '35-55', '55<=']

    num_of_prev_attempts = ['Select Number Of Previous Attempts',
                            0, 1, 2, 3, 4, 5, 6]

    is_banked = ['Select', 0, 1]

    code_module_x = ['Select First Module', 'AAA' 'BBB' 'DDD' 'FFF' 'GGG' 'CCC' 'EEE']

    code_presentation_x = ['Select First Semester (Module First)', '2013B', '2013J', '2014B', '2014J']

    code_module_y = ['Select Second Module', 'AAA', 'BBB', 'DDD', 'FFF', 'CCC', 'EEE', 'GGG']

    code_presentation_y = ['Select Semester (Module Second)', '2013B', '2013J', '2014B', '2014J']

    if request.method == 'POST':
        if request.form['gender'] == 'Select Gender' or request.form['region'] == 'Select Region'\
                or request.form['highest_education'] == 'Select Highest Education'\
                or request.form['imd_band'] == 'Select IMD Band' \
                or request.form['age_band'] == 'Select Age Group'\
                or request.form['num_of_prev_attempts'] == 'Select Number Of Previous Attempts'\
                or request.form['is_banked'] == 'Select'\
                or request.form['code_module_x'] == 'Select First Module'\
                or request.form['code_presentation_x'] == 'Select First Semester (Module First)'\
                or request.form['code_module_y'] == 'Select Second Module'\
                or request.form['code_presentation_y'] == 'Select Semester (Module Second)':
                error = 'Select all fields'
        else:
            studentInformation[0] = convertor(request.form['gender'])
            studentInformation[1] = convertor(request.form['region'])
            studentInformation[2] = convertor(request.form['highest_education'])
            studentInformation[3] = convertor(request.form['imd_band'])
            studentInformation[4] = convertor(request.form['age_band'])
            studentInformation[5] = convertor(request.form['num_of_prev_attempts'])
            studentInformation[6] = convertor(request.form['is_banked'])
            studentInformation[7] = convertor(request.form['code_module_x'])
            studentInformation[8] = convertor(request.form['code_presentation_x'])
            studentInformation[9] = convertor(request.form['code_module_y'])
            studentInformation[10] = convertor(request.form['code_presentation_y'])
            return redirect(url_for('prediction'))
    return render_template('question_form.html', error=error, gender=gender, region=region, highest_education=highest_education,
                           imd_band=imd_band, age_band=age_band, num_of_prev_attempts=num_of_prev_attempts,
                           is_banked=is_banked, code_module_x=code_module_x, code_presentation_x=code_presentation_x,
                           code_module_y=code_module_y, code_presentation_y=code_presentation_y)

@app.route('/prediction')
def prediction():
    student = np.array(studentInformation)
    studentTwoDArray = np.reshape(student, (-1, 16))
    pred_result = predictFunction(studentTwoDArray)
    # plot data
    mean_female_grade = plt.mean_female_grade
    mean_male_grade = plt.mean_male_grade
    mean_fifteen_year = plt.mean_fifteen_year
    mean_sixteen_year = plt.mean_sixteen_year
    mean_seventeen_year = plt.mean_eighteen_year
    mean_eighteen_year = plt.mean_eighteen_year
    mean_nineteen_year = plt.mean_nineteen_year
    mean_twenty_year = plt.mean_twenty_year

    return render_template('prediction.html',mean_twenty_year=mean_twenty_year,mean_nineteen_year=mean_nineteen_year,mean_eighteen_year=mean_eighteen_year,mean_seventeen_year=mean_seventeen_year,mean_sixteen_year=mean_sixteen_year,mean_fifteen_year=mean_fifteen_year,mean_female_grade=mean_female_grade, mean_male_grade = mean_male_grade ,student=student,pred_result=pred_result)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

if __name__ == "__main__":
    app.run()