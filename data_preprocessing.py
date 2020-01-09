# import libraries
# -----------------------------------------------------------------------------
import warnings
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn import tree
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import learning_curve
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

# read the data
# -----------------------------------------------------------------------------
assessments = pd.read_csv('./static/datasets/new_files/assessments.csv')
courses = pd.read_csv('./static/datasets/new_files/courses.csv')
studentAssessment = pd.read_csv('./static/datasets/new_files/studentAssessment.csv')
studentInfo = pd.read_csv('./static/datasets/new_files/studentInfo.csv')
studentRegistration = pd.read_csv('./static/datasets/new_files/studentRegistration.csv')
vle = pd.read_csv('./static/datasets/new_files/vle.csv')

# column identification
# -----------------------------------------------------------------------------
set1 = list(assessments.columns.values)
set2 = list(courses.columns.values)
set3 = list(studentAssessment.columns.values)
set4 = list(studentInfo.columns.values)
set5 = list(studentRegistration.columns.values)
set6 = list(vle.columns.values)

all_columns = [set1, set2, set3, set4, set5, set6]
columns_count = [assessments.shape, courses.shape, studentAssessment.shape,
                 studentInfo.shape, studentRegistration.shape, vle.shape]
columns_header = ['assessments', 'courses', 'studentAssessment',
                  'studentInfo', 'studentRegistration', 'vle']

d = {'Table Name': columns_header, 'Rows, Columns': columns_count, 'Column Names': all_columns}
df = pd.set_option('max_colwidth', 200)
df = pd.DataFrame(d)

# #############################################################################
# Cleaning the data
# #############################################################################

# Dropping all the missing values
# -----------------------------------------------------------------------------
assessments.dropna(inplace=True)
courses.dropna(inplace=True)
studentAssessment.dropna(inplace=True)
studentInfo.dropna(inplace=True)
studentRegistration.dropna(inplace=True)
vle.dropna(inplace=True)

columns_count = [assessments.shape, courses.shape, studentAssessment.shape,
                 studentInfo.shape, studentRegistration.shape, vle.shape]
d = {'Table Name': columns_header, 'Rows, Columns': columns_count,
     'Column Names': all_columns}
df = pd.set_option('max_colwidth', 200)
df = pd.DataFrame(d)

# Exporting the data
# -----------------------------------------------------------------------------
assessments.to_csv(r'./static/datasets/preprocessed_csv/pre_assessments.csv', index=False)
courses.to_csv(r'./static/datasets/preprocessed_csv/pre_courses.csv', index=False)
studentAssessment.to_csv(r'./static/datasets/preprocessed_csv/pre_studentAssessment.csv', index=False)
studentInfo.to_csv(r'./static/datasets/preprocessed_csv/pre_studentInfo.csv', index=False)
studentRegistration.to_csv(r'./static/datasets/preprocessed_csv/pre_studentRegistration.csv', index=False)
vle.to_csv(r'./static/datasets/preprocessed_csv/pre_vle.csv', index=False)

# Results based on Gender
# -----------------------------------------------------------------------------
gender = studentInfo.groupby(['gender'], as_index=False)
gender_count = gender['id_student'].count()
result_gender = studentInfo.groupby(['gender', 'final_result'], as_index=False)
result_gender_count = result_gender['id_student'].count()

merge = pd.merge(gender_count, result_gender_count, on='gender', how='left')
merge['i'] = round((merge['id_student_y'] / merge['id_student_x']), 2)
merge = merge[['gender', 'final_result', 'i']]

female = merge.loc[merge['gender'] == 'F']
male = merge.loc[merge['gender'] == 'M']

fig = plt.figure()

ax = fig.add_subplot(111)

female.set_index('final_result', drop=True, inplace=True)
male.set_index('final_result', drop=True, inplace=True)
female.plot(kind='bar', ax=ax, width=0.3, position=1)
male.plot(kind='bar', color='#2ca02c', ax=ax, width=0.3, position=0)

plt.xlabel('Result Status')
plt.ylabel('Result')
plt.title('Gender vs Result')
plt.legend(['Female', 'Male'])
plt.show()

# Results based on Disability
# -----------------------------------------------------------------------------
disability_ = studentInfo.groupby(['disability'], as_index=False)
disability_count = disability_['id_student'].count()
result_disability = studentInfo.groupby(['disability', 'final_result'], as_index=False)
result_disability_count = result_disability['id_student'].count()

merge = pd.merge(disability_count, result_disability_count, on='disability', how='left')
merge['i'] = round((merge['id_student_y'] / merge['id_student_x']), 2)
merge = merge[['disability', 'final_result', 'i']]

yes = merge.loc[merge['disability'] == 'Y']
no = merge.loc[merge['disability'] == 'N']

fig = plt.figure()

ax = fig.add_subplot(111)

yes.set_index('final_result', drop=True, inplace=True)
no.set_index('final_result', drop=True, inplace=True)
yes.plot(kind='bar', ax=ax, width=0.3, position=1)
no.plot(kind='bar', color='#2ca02c', ax=ax, width=0.3, position=0)

plt.xlabel('Result Status')
plt.ylabel('Result')
plt.title('Disability vs Result')
plt.legend(['Yes', 'No'])
plt.show()

# Results based on Age
# -----------------------------------------------------------------------------
age = studentInfo.groupby(['age_band'], as_index=False)
age_count = age['id_student'].count()
result_age = studentInfo.groupby(['age_band', 'final_result'], as_index=False)
result_age_count = result_age['id_student'].count()

merge = pd.merge(age_count, result_age_count, on='age_band', how='left')
merge['_'] = round((merge['id_student_y'] / merge['id_student_x']), 2)
merge = merge[['age_band', 'final_result', '_']]

merge.set_index(['age_band', 'final_result']).unstack().plot(kind='barh', stacked=True)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

plt.ylabel('Age')
plt.xlabel('Result')
plt.title('Age vs Result')
plt.legend(['Distinction', 'Fail', 'Pass', 'Withdrawn'], loc='center left', bbox_to_anchor=(1, 0.85))
plt.show()

# Results based on IMD Band
# -----------------------------------------------------------------------------
imd = studentInfo.groupby(['imd_band'], as_index=False)
imd_count = imd['id_student'].count()
result_imd = studentInfo.groupby(['imd_band', 'final_result'], as_index=False)
result_imd_count = result_imd['id_student'].count()

merge = pd.merge(imd_count, result_imd_count, on='imd_band', how='left')
merge['_'] = round((merge['id_student_y'] / merge['id_student_x']), 2)
merge = merge[['imd_band', 'final_result', '_']]

merge.set_index(['imd_band', 'final_result']).unstack().plot(kind="barh", stacked=True)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

plt.ylabel('IMD Band')
plt.xlabel('Result')
plt.title('IMD Band vs Result')
plt.legend(['Distinction', 'Fail', 'Pass', 'Withdrawn'], loc='center left', bbox_to_anchor=(1, 0.85))
plt.show()

# Results based on Highest Education
# -----------------------------------------------------------------------------
education = studentInfo.groupby(['highest_education'], as_index=False)
education_count = education['id_student'].count()
result_education = studentInfo.groupby(['highest_education', 'final_result'], as_index=False)
result_education_count = result_education['id_student'].count()

merge = pd.merge(education_count, result_education_count, on='highest_education', how='left')
merge['_'] = round((merge['id_student_y'] / merge['id_student_x']), 2)
merge = merge[['highest_education', 'final_result', '_']]

merge.set_index(['highest_education', 'final_result']).unstack().plot(kind='barh', stacked=True)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

plt.ylabel('Highest Education')
plt.xlabel('Result')
plt.title('Highest Education vs Result')
plt.legend(['Distinction', 'Fail', 'Pass', 'Withdrawn'], loc='center left', bbox_to_anchor=(1, 0.85))
plt.show()

# Results based on Region
# -----------------------------------------------------------------------------
region = studentInfo.groupby(['region'], as_index=False)
region_count = region['id_student'].count()
result_region = studentInfo.groupby(['region', 'final_result'], as_index=False)
result_region_count = result_region['id_student'].count()

merge = pd.merge(region_count, result_region_count, on='region', how='left')
merge['_'] = round((merge['id_student_y'] / merge['id_student_x']), 2)
merge = merge[['region', 'final_result', '_']]

merge.set_index(['region', 'final_result']).unstack().plot(kind="barh", stacked=True)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

plt.ylabel('Region')
plt.xlabel('Result')
plt.title('Region vs Result')
plt.legend(['Distinction', 'Fail', 'Pass', 'Withdrawn'], loc='center left', bbox_to_anchor=(1, 0.85))
plt.show()

# #############################################################################
# Predictive Models
# #############################################################################
dfs = [studentAssessment, studentInfo, studentRegistration]
df_final = reduce(lambda left, right: pd.merge(left, right, on='id_student'), dfs)
df_final['final_result'].value_counts()

df_final = df_final.drop(['date_unregistration'], axis=1)  # too many NaN values

df_final.dropna(inplace=True)
df_final['final_result'].value_counts()

df_final.to_csv(r'./static/datasets/preprocessed_csv/final.csv', index=False)

# Converting the final table to catgorical data
# -----------------------------------------------------------------------------

le = preprocessing.LabelEncoder()
df_final = df_final.apply(le.fit_transform)

# Decision Tree
# -----------------------------------------------------------------------------
X = df_final.loc[:, df_final.columns != 'final_result']
y = df_final['final_result']
xTrain, xTest, yTrain, yTest = train_test_split(X, y, train_size=0.75)

dt = tree.DecisionTreeClassifier(criterion='gini')
dt = dt.fit(xTrain, yTrain)
train_pred = dt.predict(xTrain)
test_pred = dt.predict(xTest)
print("Accuracy:{0:.3f}".format(metrics.accuracy_score(yTest, test_pred)), "\n")

# Gradient Boosting Regression
# -----------------------------------------------------------------------------
X = df_final.loc[:, df_final.columns != 'final_result']
y = df_final['final_result']
xTrain, xTest, yTrain, yTest = train_test_split(X, y, train_size=0.75)

gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=10, random_state=0, loss='huber')
gb = gb.fit(xTrain, yTrain)
print("Accuracy:{0:.3f}".format(gb.score(xTest, yTest)))

# Random Forest
# -----------------------------------------------------------------------------
X = df_final.loc[:, df_final.columns != 'final_result']
y = df_final['final_result']
xTrain, xTest, yTrain, yTest = train_test_split(X, y, train_size=0.75)

rf = RandomForestClassifier(n_estimators=10, random_state=33)
rf = rf.fit(xTrain, yTrain)
train_pred = rf.predict(xTrain)
test_pred = rf.predict(xTest)
print("Accuracy:{0:.3f}".format(metrics.accuracy_score(yTest, test_pred)), "\n")

# Model Accuracy

# Function to plot accuracy
# -----------------------------------------------------------------------------
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


# Decision Tree
# -----------------------------------------------------------------------------
plot_accuracy(dt)

# Gradient Boosting
# -----------------------------------------------------------------------------
plot_accuracy(gb)

# Random Forest
# -----------------------------------------------------------------------------
plot_accuracy(rf)

# Decision Tree Confusion Matrix
# -----------------------------------------------------------------------------
y_pred = cross_val_predict(dt, xTest, yTest)

disp = plot_confusion_matrix(dt, xTest, y_pred,
                             cmap=plt.cm.Blues,
                             normalize='true')
disp.ax_.set_title('Normalized Confusion Matrix (Decision Tree)')

print('Normalized Confusion Matrix')
print(disp.confusion_matrix)

# Random Forest Confusion Matrix
# -----------------------------------------------------------------------------
y_pred = cross_val_predict(rf, xTest, yTest)

disp = plot_confusion_matrix(rf, xTest, y_pred,
                             cmap=plt.cm.Blues,
                             normalize='true')
disp.ax_.set_title('Normalized Confusion Matrix')

print('Normalized Confusion Matrix (Random Forest)')
print(disp.confusion_matrix)
