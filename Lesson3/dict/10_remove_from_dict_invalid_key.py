user_data = {
    'name': 'Mary',
    'age': 32,
    'height': 70.9,




}

#key - values pairs

print(user_data)
print(type(user_data))    #dict

print('removing gender from dict')
del user_data['gender']  #removing gender from dict
#Error : KeyError
print(user_data)