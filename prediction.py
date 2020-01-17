import pickle
import numpy as np

X_test = np.array([118,0,18,0,83,5,0,1,12,0,3,0,2,15,0,5,0,202]).reshape(1, -1)

# loading the model from disk
#get_model()
#loaded_model = pickle.load(open('random_forest_model.sav', 'rb'))
#result = loaded_model.predict(X_test)
#print(result)

def getModel(model_name):
    if model_name == 'decision-tree':
        model = 'decision_tree_model.sav'
    elif model_name == 'gradient-boosting':
        model = 'gradient_boosting_model.sav'
    elif model_name == 'random-forest':
        model = 'random_forest_model.sav'

    return pickle.load(open(model, 'rb'))

def predict(model_name):
    model = getModel(model_name)
    grade = model.predict(X_test)
    print("The predicted grade is: {}".format(grade[0]))

