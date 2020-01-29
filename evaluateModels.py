# evaluating the machine learning models (jupyter notebook)

#imports

import json
import pickle
import numpy as np
import pandas as pd
import scikitplot as skplt
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import learning_curve
from sklearn.model_selection import train_test_split

df_final = pd.read_csv('static/datasets/final_pre_processed_data_encoded.csv')
X = df_final.loc[:, df_final.columns != 'final_result']
y = df_final['final_result']
xTrain, xTest, yTrain, yTest = train_test_split(X, y,train_size = 0.75)

# read the pre-trained model

def getModel(model_name):
    if model_name == 'decision-tree':
        model = 'models/decision_tree_model.sav'
    elif model_name == 'gradient-boosting':
        model = 'models/gradient_boosting_model.sav'
    elif model_name == 'random-forest':
        model = 'models/random_forest_model.sav'
    elif model_name == 'naive-bayes':
        model = 'models/naive_bayes_model.sav'
    elif model_name == 'svm':
        model = 'models/svm_model.sav'

    return pickle.load(open(model, 'rb'))


# Function to plot accuracy

def plot_accuracy(model):
    train_sizes, train_scores, test_scores = learning_curve(model, xTrain, yTrain, n_jobs=-1,
                                                            train_sizes=np.linspace(.1, 1.0, 5), verbose=0)

    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    plt.figure()
    plt.gca().invert_yaxis()
    plt.grid()
    plt.ylim(0.0, 1.1)
    plt.title("Accuracy Plot")
    plt.xlabel("Testing")
    plt.ylabel("Accuracy %")

    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1)
    plt.plot(train_sizes, test_mean, 'bo-', color="r", label="Test Score")
    return plt

# decision tree
dt = getModel('decision-tree')
plt = plot_accuracy(dt)
#plt.savefig('static/images/decision_tree_acc.png')

y_pred = cross_val_predict(dt, xTest, yTest)
skplt.metrics.plot_confusion_matrix(yTest, y_pred, normalize=True)
#plt.savefig('static/images/decision_tree_cf.png')

# gradient boosting
gb = getModel('gradient-boosting')
plt = plot_accuracy(gb)
#plt.savefig('static/images/decision_tree_acc.png')

y_pred = cross_val_predict(dt, xTest, yTest)
skplt.metrics.plot_confusion_matrix(yTest, y_pred, normalize=True)
#plt.savefig('static/images/gradient_boosting_cf.png')

# random forest
rf = getModel('random-forest')
plt = plot_accuracy(rf)
#plt.savefig('static/images/decision_tree_acc.png')

y_pred = cross_val_predict(dt, xTest, yTest)
skplt.metrics.plot_confusion_matrix(yTest, y_pred, normalize=True)
#plt.savefig('static/images/random_forest_cf.png')

# naive-bayes
nb = getModel('naive-bayes')
plt = plot_accuracy(rf)
#plt.savefig('static/images/decision_tree_acc.png')

y_pred = cross_val_predict(dt, xTest, yTest)
skplt.metrics.plot_confusion_matrix(yTest, y_pred, normalize=True)
#plt.savefig('static/images/naive_bayes_cf.png')

# svm
svm = getModel('svm')
plt = plot_accuracy(svm)
#plt.savefig('static/images/decision_tree_acc.png')

y_pred = cross_val_predict(dt, xTest, yTest)
skplt.metrics.plot_confusion_matrix(yTest, y_pred, normalize=True)
#plt.savefig('static/images/svm_cf.png')
