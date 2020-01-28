# pre-process the data

#imports

import pickle
import pydotplus
import numpy as np
import pandas as pd
from scipy import stats
from functools import reduce
import matplotlib.pyplot as plt
from sklearn import preprocessing
from IPython.display import Image  
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

# reading the files
assessments = pd.read_csv('static/datasets/data/assessments.csv')
courses = pd.read_csv('static/datasets/data/courses.csv')
studentAssessment = pd.read_csv('static/datasets/data/studentAssessment.csv')
studentInfo = pd.read_csv('static/datasets/data/studentInfo.csv')
studentRegistration = pd.read_csv('static/datasets/data/studentRegistration.csv')
# big file: can't be pushed to github
studentVle = pd.read_csv('static/datasets/data/studentVle.csv', nrows=999999)
vle = pd.read_csv('static/datasets/data/vle.csv')

set1 = list(assessments.columns.values)
set2 = list(courses.columns.values)
set3 = list(studentAssessment.columns.values)
set4 = list(studentInfo.columns.values)
set5 = list(studentRegistration.columns.values)
set6 = list(studentVle.columns.values)
set7 = list(vle.columns.values)

all_columns = [set1, set2, set3, set4, set5, set6, set7]
columns_count = [assessments.shape,courses.shape,studentAssessment.shape, studentInfo.shape, studentRegistration.shape, studentVle.shape, vle.shape]
columns_header = ['assessments', 'courses', 'studentAssessment', 'studentInfo', 'studentRegistration', 'studentVle', 'vle' ]

d = {'Table Name':columns_header,'Rows, Columns': columns_count,'Column Names':all_columns}
df = pd.set_option('max_colwidth', 200)
df = pd.DataFrame(d)

# cleaning the data
# Dropping all the missing values
assessments.dropna(inplace=True)
courses.dropna(inplace=True)
studentAssessment.dropna(inplace=True)
studentInfo.dropna(inplace=True)
studentRegistration.dropna(inplace=True)
studentVle.dropna(inplace=True)
vle.dropna(inplace=True)

columns_count = [assessments.shape,courses.shape,studentAssessment.shape, studentInfo.shape, studentRegistration.shape, studentVle.shape, vle.shape]
d = {'Table Name':columns_header,'Rows, Columns': columns_count,'Column Names':all_columns}
df = pd.set_option('max_colwidth', 200)
df = pd.DataFrame(d)

dfs = [studentAssessment, studentInfo, studentRegistration]
df_final = reduce(lambda left,right: pd.merge(left,right,on='id_student'), dfs)
df_final['final_result'].value_counts()

df_final = df_final.drop(['date_registration','date_unregistration', 'id_assessment', 'id_student', 'date_submitted', 'score', 'studied_credits'],axis =1) # too many NaN values

df_final.dropna(inplace=True)
df_final['final_result'].value_counts()

df_final_original = df_final

# converting the final table to labelEncoder
le = preprocessing.LabelEncoder()
df_final = df_final.apply(le.fit_transform)

# chi-square test
#creating a list of features
features = df_final.columns.tolist()
features.remove('final_result')
target = 'final_result'

# computing chi-square test for independence
df2 = pd.DataFrame(columns=["Feature", "P Value (Score)", "Correlation"])

for col in features:
    print(col)
    contingency_table = pd.crosstab(df_final[target], df_final[col], margins=True)
    f_obs = np.array([contingency_table.iloc[0][:-1].values, contingency_table.iloc[1][0:-1].values])
    p_value = stats.chi2_contingency(f_obs)[1]

    if p_value <= 0.05:
        correlation = 'Yes'
    else:
        correlation = 'No'

    data = {'Feature': col, 'P Value (Score)': p_value, 'Correlation': correlation}
    df2 = df2.append(data, ignore_index=True)

print(df2)

# dropping disability (non significant)
df_final = df_final.drop(['disability'],axis =1)
df_final_original = df_final_original.drop(['disability'],axis =1)

#df_final.to_csv("static/datasets/final_pre_processed_data_encoded.csv", index=False)
#df_final_original.to_csv("static/datasets/final_pre_processed_data.csv", index=False)