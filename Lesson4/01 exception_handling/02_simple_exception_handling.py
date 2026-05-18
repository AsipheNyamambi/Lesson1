try:
    num1 = int(input("Enter first number 1: "))
    num2 = int(input("Enter second number 2 : "))


    #answer = calculations.add(10,20)
    answer = num1 + num2
    print(answer)

    #if you enter a letter, this program will crash
    #ValueError

except ValueError as e:
    print(e)
    print("Invalid data entered")

except Exception as e:
       print(e)
       print("something went wrong")
