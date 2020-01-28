# evaluating the machine learning models

#imports

import json
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

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

# decision tree
dt = getModel('decision-tree')
plot_accuracy(dt)

# gradient boosting
gb = getModel('gradient-boosting')
plot_accuracy(gb)

# random forest
rf = getModel('random-forest')
plot_accuracy(rf)

# naive-bayes
nb = getModel('naive-bayes')
plot_accuracy(rf)

# svm
svm = getModel('svm')
plot_accuracy(svm)