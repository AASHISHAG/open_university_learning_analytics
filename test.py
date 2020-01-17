def switch_func(value):
    return {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }.get(value)

# take user input
inp = input('input a character : ')

print('The result for inp is : ', switch_func(inp))