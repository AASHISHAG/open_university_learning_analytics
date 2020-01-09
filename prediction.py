import pickle
import numpy as np

X_test = np.array([118,0,18,0,83,5,0,1,12,0,3,0,2,15,0,5,0,202]).reshape(1, -1)

# loading the model from disk
loaded_model = pickle.load(open('random_forest_model.sav', 'rb'))
result = loaded_model.predict(X_test)
print(result)

