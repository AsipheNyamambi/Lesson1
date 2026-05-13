#homework
#User1 information
name = input('enter user1 name')
age = int (input('enter user1 age'))
height = float (input('enter user1 Height'))

#Display user1 information
print(f'You are {name} . You are {age} years old . Your height is {height} cm')

#User2 information
name2 = input('enter user2 name')
age2 = int (input('enter user2 age'))
height2 = float (input('enter user2 Height'))

#Display user2 information
print(f'You are {name2} . You are {age2} years old . Your height is {height2} cm')

#Calculate the total height of both combined users
Total = float (height + height2)
print(f'Total height of both combined users : {Total} cm')
