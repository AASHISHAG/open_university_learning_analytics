# imports

import pickle
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import metrics
from labelEncoder import encode
from sklearn.model_selection import train_test_split

# sequence of the columns defined on the web interface

sequence = [
    'gender',
    'region',
    'highest_education',
    'imd_band',
    'age_band',
    'num_of_prev_attempts',
    'is_banked',
    'code_module_x',
    'code_presentation_x',
    'code_module_y',
    'code_presentation_y',
    ]


# read the pre-trained model

def getModel(model_name):
    if model_name == 'decision-tree':
        model = 'models/decision_tree_model.sav'
    elif model_name == 'gradient-boosting':
        model = 'models/gradient_boosting_model.sav'
    elif model_name == 'random-forest':
        model = 'models/random_forest_model.sav'

    return pickle.load(open(model, 'rb'))


# predict student result by using the pre-trained model trained on all the features

def predict_model(model_name, student_information):
    model = getModel(model_name)
    student_information = np.array(student_information).reshape(1, -1)
    grade = model.predict(student_information)
    grade = encode(grade[0])
    print('The predicted grade is: {}'.format(grade))
    return grade


# predict student result by training on any N features

def predict(student_information):
    (model, accuracy) = train_model(student_information)
    cleaned_student_information = [x for x in student_information
                                   if str(x) != 'None']
    student_information = \
        np.array(cleaned_student_information).reshape(1, -1)
    grade = model.predict(student_information)
    grade = encode(grade[0])
    print('The predicted grade is: {}'.format(grade))
    return (grade, accuracy)


# train the machine learning model

def train_model(student_information):
    df_final = \
        pd.read_csv('static/datasets/final_pre_processed_data_encoded.csv'
                    )
    columns = get_columns(student_information)
    X = df_final[columns]
    y = df_final['final_result']
    (xTrain, xTest, yTrain, yTest) = train_test_split(X, y,
            train_size=0.75)

    # #dt = tree.DecisionTreeClassifier(criterion='gini')

    dt = tree.DecisionTreeClassifier()
    dt = dt.fit(xTrain, yTrain)
    test_pred = dt.predict(xTest)
    accuracy = metrics.accuracy_score(yTest, test_pred)
    return (dt, accuracy)


# get name of the columns selected by the user

def get_columns(student_information):
    columns = []
    count = 0
    for i in student_information:
        if i != None:
            columns.append(sequence[count])
        count += 1
    return columns
