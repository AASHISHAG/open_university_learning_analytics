import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
print("libraries imported")

#read data
df = pd.read_csv("./static/datasets/dataset_main.csv", engine='python',sep=',')



# add new feature to use it for classification
grades = df['G3'].values
labels = []

for grade in grades:
    if grade >=17:
        labels.append('very good')
    elif grade < 17 and grade >= 15:
        labels.append('good')
    elif grade < 15 and grade >= 10:
        labels.append('average')
    elif grade < 10:
        labels.append('bad')

#encoding the data
enc = LabelEncoder()
for item in df:
    data_raw = df[item].values
    df[item] = enc.fit_transform(data_raw)

enc_labels = enc.fit_transform(labels)

print(df.head(4))
df = df.values
#print(df['item'].head())
#preparing test data
X_train, X_test, y_train, y_test = train_test_split(df[:,:16],enc_labels, stratify=enc_labels,random_state=0,test_size=0.20)

#report func
def report(clf, X_train, y_train, X_test, y_test,M_name):
    print("+++++report of the model+++++")
    print(M_name)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print('Precision score: {:3f}'.format(precision_score(y_test, y_pred, average='macro')))
    print('Prediction Accuracy: {:3f}'.format(accuracy_score(y_test, y_pred)))
    print('Recall score: {:3f}'.format(recall_score(y_test, y_pred, average='macro')))
    print('F1 score: {:3f}'.format(f1_score(y_test, y_pred, average='macro')))


#models
lr = LogisticRegression()
report(lr, X_train, y_train, X_test, y_test,"LogisticRegressio")

knn = KNeighborsClassifier()
report(knn, X_train, y_train, X_test, y_test, "KNeighborsClassifier")

validation_data = [[1,1,2,1,2,1,2,2,1,2,1,1,2,1,2,1]]
print(X_train)
def predictFunction(data_predicit):
    result =lr.predict(data_predicit)
    if result[0] == 0:
        return 'Average'
    if result[0] == 1:
        return 'Bad'
    if result[0] == 2:
        return 'Good'
    if result[0] == 3:
        return 'Very good'
    #print("the predicted grade is {}".format(result[0]))
    #return result[0]

predictFunction(validation_data)
# save model with picklee
