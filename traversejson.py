import json

'''
Gender=0
Region=0
HighestEducation=0
IMDBand=0
AgeGroup=0
NumberOfPreviousAttempts=0
Semester=0
FirstModule=0
SemesterFirstModule=0
SecondModule=0
SemesterSecondModule=0
'''

def ffff (data, Gender, Region, HighestEducation, IMDBand, AgeGroup, NumberOfPreviousAttempts, Semester,
          FirstModule, SemesterFirstModule, SecondModule, SemesterSecondModule):
    check = 0
    for (k, v) in data.items():
        if (k != 'name'):
            return ffff(v[check], Gender, Region, HighestEducation, IMDBand, AgeGroup, NumberOfPreviousAttempts, Semester,
          FirstModule, SemesterFirstModule, SecondModule, SemesterSecondModule)
        else:
            if (" of ") not in v:
                v = v.replace(" ", "")
                v = v.replace("(", "")
                v = v.replace(")", "")
            else:
                return v

            if(eval(v)):
                check=1
            else:
                check=0


def rules123(Gender=0, Region=0, HighestEducation=0, IMDBand=0, AgeGroup=0, NumberOfPreviousAttempts=0, Semester=0,
          FirstModule=0, SemesterFirstModule=0, SecondModule=0, SemesterSecondModule=0):
    with open('./static/datasets/rules.json') as json_file:
        data = json.load(json_file)
        print(data)
        a = ffff(data, Gender, Region, HighestEducation, IMDBand, AgeGroup, NumberOfPreviousAttempts, Semester,
          FirstModule, SemesterFirstModule, SecondModule, SemesterSecondModule)
        print("path: "+str(a))
        return a



