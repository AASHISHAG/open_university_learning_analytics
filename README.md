## Table of content 
- [OULA (intelligent grade prediction system)](#headers)
- [based on Open University dataset](#headers2)
- [Requirements and preparation](#headers2)
- [App Structure](#headers3)
- [code explanation](#headers4)

<a name="headers"/>

youtube video about project
https://www.youtube.com/

![Logo](static/images/logo.png)
<img src="static/images/logo.png" width="100">

## OULA (intelligent grade prediction system)
Grade prediction system based on trend of the recorded data in database. User select its habit then get the grade closest to the final result.

<a name="headers2"/>

## Requirements and preparation
This project is based on the following technology:
* Data
  + Pandas
  + Numpy
  
* Model
  + Sikit-learn
  
* Web side
  + Flask
  + Bootstrap

* visualisation
  + Chartjs
  + D3

* Database
  + mongodb


<a name="headers3"/>

# App Structure
we can seprate this project (Flask framework) to several main part with different functionality.

App (OULA):
  + static (folder)
    + css (folder)
      + bootstrap
    + datasets (folder)
      + dataset_main.csv // main dataset for making model
    + images (folder)
      + Logo.png 
      + ki.jpg
    + javascript (folder)
      + viz.js // main javascript file for making charts
  + template (folder)
    + index.html
    + prediction.html // page of showing the prediction result
    + question_form.html // the form for getting user input
  + Convertor.py
  + Model_classification.py // classifier model
  + plot.py // preparing data to use for plotting
  + server.py // application server backend part
  

<a name="headers4"/>

# Step 1
### Data prepration (Model_classification.py)
for making our model and use it for the prediction we need to first prepare the data for process. we are dealing with data using "pandas", "numpy" , "sklearn"
so we need to import this library:

```ruby
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

```
and then we are reading the data and encoding the categorical data in order to give them to model in training process:

```ruby
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

```
# Step 2
### creating our model (Model_classification.py)
we are using two clasifier in this project, and then used the most accurate one. we are using sci-kit learn python library.

```ruby

import pandas as pd
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

```
and then later we can use predict model to get the prediction result based on new data. prediction function just change the numerical output to categorical one
```ruby

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

```
# Step 3
### Web structure preparation (server.py)
so for using our model on our web application we are using "Flask" python framework as our web back-end. so everything is happening in server.py file. getting new data from front-end file and send it to server and then calling prediction function and send it again to front-end to show it up.

```ruby
@app.route('/prediction')
def prediction():
    student = np.array(studentInfo)
    studentTwoDArray = np.reshape(student, (-1, 16))
    pred_result = predictFunction(studentTwoDArray)
    
    return render_template('prediction.html',student=student,pred_result=pred_result)

```

# Step 4
### Visualization part- charts and plots(server.py and plot.py and viz.js)
in visualisation part we just tried to provide few chart to make the data more understandable maybe will help user to get better view from predicted result. we used "chartjs and D3" javascript libraries to visualize the data.

we defined few functions for few chart then later we plot them just by calling this function:
1. ageResultPlot: plot result distribution regarding age

```ruby
function agePlot(data_one,data_two, data_three, data_four, data_five){

var ctx = document.getElementById('ageChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'doughnut',

    // The data for our dataset
    data: {
        labels: ["15", "16","17","18","19","20"],
        datasets: [{
            label: "Avarage grade based on gender",
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
            borderColor: 'rgb(255, 99, 132)',
            data: [data_one,data_two, data_three, data_four, data_five,5],
        }]
    },

    // Configuration options go here
    options: {}
});
}
```

# Run the code
after we install below requirements on our system:
  * sci-kit learn
  * Flask
  * Numpy
  * Panda
  * html5lib
  * pyplot
  * pymongo
  * dnspython

  
you can simply run the server.py file and then server will run on you localhost. then just open Browser and type your local host IP with the port (localhost:5000) and enjoy the application

# Contributor
Sameh Frihat
Aashish Agarwal
Shoeb Ahmed Joarder
Seyedemarzie Mirhashemi