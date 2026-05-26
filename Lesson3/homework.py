#homework


def display_total_height(h1, h2):
    total = h1 + h2
    print(f'Total height of both combined users : {total} cm')
    return total

#User1 information
name = input('enter user1 name')
age = int (input('enter user1 age'))
height = float (input('enter user1 Height'))

user1 = [name, age, height]
print(user1)
print(type(user1))

for user in user1:
    print(user)
    print(type(user))
print(f'You are {name} . You are {age} years old . Your height is {height} cm')

#User2 information
name2 = input('enter user2 name')
age2 = int (input('enter user2 age'))
height2 = float (input('enter user2 Height'))

user2 = {
    'name': name2,
    'age': age2,
    'height': height2
}
print(user2)
print(type(user2))

for user in user2:
    print(user)
    print(type(user))
print(f'You are {name2} . You are {age2} years old . Your height is {height2} cm')


display_total_height(height, height2)



