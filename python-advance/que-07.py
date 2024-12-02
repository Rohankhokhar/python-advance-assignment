#  7) Write a Python program to handle exceptions in a calculator

try:
    num1 = int(input("enter num1 value:"))
    num2 = int(input("enter num2 value:"))
    opretor = input("enter opretor (+,-,*,/):")

    if opretor == '+':
        res = num1 + num2
    elif opretor == '-':
        res = num1 - num2 
    elif opretor == '*':
        res = num1 * num2 
    elif opretor == '/':
        res = num1 / num2
    print(res)
except ZeroDivisionError:
    print("ZeroDivisionError : can not divid by zero")
except Exception as err:
    print(f"error:{err}")    


    