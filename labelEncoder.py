# LabelEncoder

def encode(value):
    return {
        'Female': 0,
        'Male': 1,
        'East Anglian Region': 0,
        'East Midlands Region': 1,
        'Ireland': 2,
        'London Region': 3,
        'North Region': 4,
        'North Western Region': 5,
        'Scotland': 6,
        'South East Region': 7,
        'South Region': 8,
        'South West Region': 9,
        'Wales': 10,
        'West Midlands Region': 11,
        'Yorkshire Region': 12,
        'A Level or Equivalent': 0,
        'No Formal Qualification': 1,
        'Higher Education Qualification': 2,
        'Post Graduation Qualification': 3,
        'A Level or Equivalent': 4,
        '0-10%': 0,
        '10%-20%': 1,
        '20%-30%': 2,
        '30%-40%': 3,
        '40%-50%': 4,
        '50%-60%': 5,
        '60%-70%': 6,
        '70%-80%': 7,
        '80%-90%': 8,
        '90%-100%': 9,
        '0-35': 0,
        '35-55': 1,
        '55<=': 2,
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        'AAA': 0,
        'BBB': 1,
        'DDD': 2,
        'FFF': 3,
        'GGG': 4,
        'CCC': 5,
        'EEE': 6,
        '2013B': 0,
        '2013J': 1,
        '2014B': 2,
        '2014J': 3,
    }.get(value)