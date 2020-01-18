import pickle
import numpy as np
from labelEncoder import encode

#X_test = np.array([118,0,18,0,83,5,0,1,12,0,3,0,2,15,0,5,0,202]).reshape(1, -1)

# loading the model from disk
#get_model()
#loaded_model = pickle.load(open('random_forest_model.sav', 'rb'))
#result = loaded_model.predict(X_test)
#print(result)

def getModel(model_name):
    if model_name == 'decision-tree':
        model = 'models/decision_tree_model.sav'
    elif model_name == 'gradient-boosting':
        model = 'models/gradient_boosting_model.sav'
    elif model_name == 'random-forest':
        model = 'models/random_forest_model.sav'

    return pickle.load(open(model, 'rb'))

def predict(model_name, student_information):
    model = getModel(model_name)
    student_information = np.array(student_information).reshape(1, -1)
    grade = model.predict(student_information)
    grade = encode(grade[0])
    print("The predicted grade is: {}".format(grade))
    return grade

