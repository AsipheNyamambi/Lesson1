#option 2          importing whole file single function

#import calculation

from calculations import add,subtract

num1 = int(input("Enter first number 1: "))
num2 = int(input("Enter second number 2 : "))


#answer = calculations.add(10,20)
answer = add(num1,num2)
print(answer)

answer = subtract(num1,num2)
print(answer)