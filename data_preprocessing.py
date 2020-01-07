# import libraries
import pandas as pd

# read the data
assessments = pd.read_csv('./static/datasets/assessments.csv')
courses = pd.read_csv('./static/datasets/courses.csv')
studentAssessment = pd.read_csv('./static/datasets/studentAssessment.csv')
studentInfo = pd.read_csv('./static/datasets/studentInfo.csv')
studentRegistration = pd.read_csv('./static/datasets/studentRegistration.csv')
vle = pd.read_csv('./static/datasets/vle.csv')

# column identification
set1 = list(assessments.columns.values)
set2 = list(courses.columns.values)
set3 = list(studentAssessment.columns.values)
set4 = list(studentInfo.columns.values)
set5 = list(studentRegistration.columns.values)
set6 = list(vle.columns.values)

all_columns = [set1, set2, set3, set4, set5, set6]
columns_count = [assessments.shape, courses.shape, studentAssessment.shape,
                 studentInfo.shape, studentRegistration.shape, vle.shape]
columns_header = ['assessments', 'courses', 'studentAssessment',
                  'studentInfo', 'studentRegistration', 'vle']

d = {'Table Name': columns_header, 'Rows, Columns': columns_count, 'Column Names': all_columns}
df = pd.set_option('max_colwidth', 200)
df = pd.DataFrame(d)

# Cleaning the data
# Dropping all the missing values
assessments.dropna(inplace=True)
courses.dropna(inplace=True)
studentAssessment.dropna(inplace=True)
studentInfo.dropna(inplace=True)
studentRegistration.dropna(inplace=True)
vle.dropna(inplace=True)

columns_count = [assessments.shape, courses.shape, studentAssessment.shape,
                 studentInfo.shape, studentRegistration.shape, vle.shape]
d = {'Table Name': columns_header, 'Rows, Columns': columns_count,
     'Column Names': all_columns}
df = pd.set_option('max_colwidth', 200)
df = pd.DataFrame(d)

# Exporting the data
assessments.to_csv(r'./static/datasets/preprocessed_csv/pre_assessments.csv', index=False)
courses.to_csv(r'./static/datasets/preprocessed_csv/pre_courses.csv', index=False)
studentAssessment.to_csv(r'./static/datasets/preprocessed_csv/pre_studentAssessment.csv', index=False)
studentInfo.to_csv(r'./static/datasets/preprocessed_csv/pre_studentInfo.csv', index=False)
studentRegistration.to_csv(r'./static/datasets/preprocessed_csv/pre_studentRegistration.csv', index=False)
vle.to_csv(r'./static/datasets/preprocessed_csv/pre_vle.csv', index=False)
