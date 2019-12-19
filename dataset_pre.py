#Importing Libraries
import csv
import pandas as pd
print('Libraries Imported')


# get the raw dataset
dataset = pd.read_csv('./static/datasets/student-por.csv', header = None)
print("csv has been read")

# remove double quotes
for i, col in enumerate(dataset.columns):
    dataset.iloc[:, i] = dataset.iloc[:, i].str.replace('"', '')

# split all features to diffrent column
newDatasets = dataset[0].str.split(";", n = 32, expand = True)
print("double quotes removed and data was separated")

# open new csv file to save clean one
outfile = open("./static/datasets/student-por-clean.csv", "w")
writer = csv.writer(outfile)

# dropping passed columns
# newDatasets.drop([1], axis = 1, inplace = True)

for column  in newDatasets.columns:
    for idx in newDatasets[column].index:
        x = newDatasets.at[idx, column]

# save it on new csv
newDatasets.to_csv(outfile)

print(newDatasets.head())
print("csv saved")
