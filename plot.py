import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import plotly.tools as tls
from html5lib._trie import py

#data loading


df = pd.read_csv("./static/datasets/dataset_main.csv", engine='python',sep=',')


# data split based on gender
m_data = df.loc[df['sex'] == 'M']
f_data = df.loc[df['sex'] == 'F']


# grade split based on gender
male_grade = m_data["G3"]
female_grade = f_data["G3"]

#mean of grade based on gender
mean_male_grade = male_grade.mean()
mean_female_grade = female_grade.mean()

# gender counter
sex = df['sex'].values
male_counter = Counter(sex)["M"]
female_counter = Counter(sex)["F"]
print(mean_female_grade)
print(mean_male_grade)


# ##################################
# plot grade based on gender
# ##################################
# objects = ('M','F')
# y_pos = np.arange(len(objects))
# performance = [mean_male_grade,mean_female_grade]
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Average')
# plt.title('grade average based on gender')
#
#
# plt.show()


# ##################################
# end
# ##################################

# age
fifteen_year = df.loc[df["age"] == 15]
sixteen_year = df.loc[df["age"] == 16]
seventeen_year = df.loc[df["age"] == 17]
eighteen_year = df.loc[df["age"] == 18]
nineteen_year = df.loc[df["age"] == 19]
twenty_year = df.loc[df["age"] == 20]

# mean based on age
mean_fifteen_year = fifteen_year["G3"].mean()
mean_sixteen_year = sixteen_year["G3"].mean()
mean_seventeen_year = seventeen_year["G3"].mean()
mean_eighteen_year  = eighteen_year ["G3"].mean()
mean_nineteen_year  = nineteen_year ["G3"].mean()
mean_twenty_year = twenty_year["G3"].mean()



# plot average Grade based on age


