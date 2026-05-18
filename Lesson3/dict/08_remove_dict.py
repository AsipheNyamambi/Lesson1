user_data = {
    'name': 'Mary',
    'age': 32,
    'height': 70.9,


}

#key - values pairs
print(user_data)
print(type(user_data))    #dict

print()

print('Removing name from dict')
del user_data['name']     #removing from dict
print(user_data)