# def sex_con(user_input_raw):
#     con = 1
#     if user_input_raw == 'M':
#         con = 0
#     else:con=1
#     return con
#
# def age_con(user_input_raw):
#     con = 1
#     if user_input_raw == 15:
#         con = 0
#     elif user_input_raw == 16:
#         con = 1
#     elif user_input_raw == 17:
#         con = 2
#     elif user_input_raw == 18:
#         con = 3
#     elif user_input_raw == 19:
#         con = 4
#     elif user_input_raw == 20:
#         con = 5
#     elif user_input_raw == 21:
#         con = 6
#     return con
#
# def travelTime_con(user_input_raw):
#     con = 1
#     if user_input_raw == 1:
#         con = 0
#     elif user_input_raw == 2:
#         con = 1
#     elif user_input_raw == 3:
#         con = 2
#     elif user_input_raw == 4:
#         con = 3
#     elif user_input_raw == 5:
#         con = 4
#     return con
#
# def studyTime_con(user_input_raw):
#     con = 1
#     if user_input_raw == 1:
#         con = 0
#     elif user_input_raw == 2:
#         con = 1
#     elif user_input_raw == 3:
#         con = 2
#     elif user_input_raw == 4:
#         con = 3
#     elif user_input_raw == 5:
#         con = 4
#     return con

def convertor(user_input_raw):
    #con = int(user_input_raw)
    con = 1
    if user_input_raw == '1':
        con = 0
    elif user_input_raw == '2':
        con = 1
    elif user_input_raw == '3':
        con = 2
    elif user_input_raw == '4':
        con = 3
    elif user_input_raw == '5':
        con = 4
    if user_input_raw == '15':
        con = 0
    elif user_input_raw == '16':
        con = 1
    elif user_input_raw == '17':
        con = 2
    elif user_input_raw == '18':
        con = 3
    elif user_input_raw == '19':
        con = 4
    elif user_input_raw == '20':
        con = 5
    elif user_input_raw == '21':
        con = 6
    elif user_input_raw == 'M':
        con = 0
    elif user_input_raw == 'F':
        con = 1
    elif user_input_raw == 'yes':
        con = 0
    elif user_input_raw == 'no':
        con = 1
    if user_input_raw == '0':
        con = 0
    elif user_input_raw == '1':
        con = 1
    elif user_input_raw == '2':
        con = 2
    elif user_input_raw == '3':
        con = 3
    elif user_input_raw == '4':
        con = 4
    elif user_input_raw == '5':
        con = 5
    elif user_input_raw == '6':
        con = 6
    elif user_input_raw == '7':
        con = 7
    elif user_input_raw == '8':
        con = 8
    elif user_input_raw == '9':
        con = 9
    elif user_input_raw == '10':
        con = 10
    elif user_input_raw == '11':
        con = 11
    elif user_input_raw == '12':
        con = 12
    elif user_input_raw == '13':
        con = 13
    elif user_input_raw == '14':
        con = 14
    elif user_input_raw == '15':
        con = 15
    elif user_input_raw == '16':
        con = 16
    elif user_input_raw == '18':
        con = 17
    elif user_input_raw == '21':
        con = 18
    elif user_input_raw == '22':
        con = 19
    elif user_input_raw == '24':
        con = 20
    elif user_input_raw == '26':
        con = 21
    elif user_input_raw == '30':
        con = 22
    elif user_input_raw == '32':
        con = 23
    return con