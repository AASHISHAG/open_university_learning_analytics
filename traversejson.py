import json

num_of_prev_attempts = 1

with open('rules.json') as json_file:
    data = json.load(json_file)
    for (k, v) in data.items():
        print("Key: " + k)
        print("Value: " + str(v))

        if (k == 'children'):
            for (k, v) in v.items():
                print("Key: " + k)
                print("Value: " + str(v))