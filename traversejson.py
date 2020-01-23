import json

dict = {}

Gender=0
Region=5
HighestEducation=3
IMDBand=0
AgeGroup=2
NumberOfPreviousAttempts=1
Semester=1
FirstModule=3
SemesterFirstModule=0
SecondModule=0
SemesterSecondModule=0

def ffff (data):
    check = 0
    for (k, v) in data.items():
        if (k != 'name'):
            print(v)
            print("Value "+str(check)+":"+ str(v[check]))
            return ffff(v[check])
        else:
            if (" of ") not in v:
                v = v.replace(" ", "")
                v = v.replace("(", "")
                v = v.replace(")", "")
            else:
                print("soso")
                print(v)
                return v

            print("Value: " + str(eval(v)))
            if(eval(v)):
                check=1
            else:
                check=0



        #print("Key: " + k)
        '''if (k != 'name'):
            print("Value 0: " + str(v[0]))
            print("Value 1: " + str(v[1]))
        else:
            print("Value: "+str( eval(v)))'''



with open('./static/datasets/rules.json') as json_file:
    data = json.load(json_file)
    print("Data: {}".format(data))
    print(" res is : "+str(ffff(data)))
    '''for (k, v) in data.items():
        print("Key: " + k)
        if (k != 'name'):
            print("Value 0: " + str(v[0]))
            print("Value 1: " + str(v[1]))
        else:
            print("Value: "+str( eval(v)))
    '''



