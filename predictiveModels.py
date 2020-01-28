# machine learning models

#imports

import pickle
import pandas as pd
from sklearn import svm
from sklearn import tree
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

df_final = pd.read_csv('static/datasets/final_pre_processed_data_encoded.csv')

# input features, output result and train, test split
X = df_final.loc[:, df_final.columns != 'final_result']
y = df_final['final_result']
xTrain, xTest, yTrain, yTest = train_test_split(X, y,train_size = 0.75)

# decision tree
dt = tree.DecisionTreeClassifier(criterion='gini')
dt = dt.fit(xTrain, yTrain)
train_pred = dt.predict(xTrain)
test_pred = dt.predict(xTest)
print("Accuracy Decision Tree:{0:.3f}".format(metrics.accuracy_score(yTest, test_pred)),"\n")

# gradient boosting
gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=10, random_state=0, loss='huber')
gb = gb.fit(xTrain, yTrain)
print("Accuracy Gradient Boosting:{0:.3f}".format(gb.score(xTest, yTest)))

# random forest
rf = RandomForestClassifier(n_estimators=10,random_state=33)
rf = rf.fit(xTrain, yTrain)
train_pred = rf.predict(xTrain)
test_pred = rf.predict(xTest)
print("Accuracy Random Forest:{0:.3f}".format(metrics.accuracy_score(yTest, test_pred)),"\n")

# naive bayes
gnb = GaussianNB()
gnb = gnb.fit(xTrain, yTrain)
train_pred = gnb.predict(xTrain)
test_pred = gnb.predict(xTest)
print("Accuracy GaussianNB:{0:.3f}".format(metrics.accuracy_score(yTest, test_pred)),"\n")

# svm
svm = svm.SVC(decision_function_shape='ovo')
svm = svm.fit(xTrain, yTrain)
train_pred = svm.predict(xTrain)
test_pred = svm.predict(xTest)
print("Accuracy SVM:{0:.3f}".format(metrics.accuracy_score(yTest, test_pred)),"\n")

# saving the models
filename = 'models/decision_tree_model.sav'
pickle.dump(dt, open(filename, 'wb'))

filename = 'models/gradient_boosting_model.sav'
pickle.dump(gb, open(filename, 'wb'))

filename = 'models/random_forest_model.sav'
pickle.dump(rf, open(filename, 'wb'))

filename = 'models/naive_bayes_model.sav'
pickle.dump(gnb, open(filename, 'wb'))

filename = 'models/svm_model.sav'
pickle.dump(svm, open(filename, 'wb'))