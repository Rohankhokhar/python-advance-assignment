try :
    file_name = input("enter existing file name:")
    f1 = open(file_name,'r')
    data = f1.read()
    print(data)

    num1 = int(input ("enter a number:"))
    num2 = int(input ("enter a number:"))
    res = num1/num2
    print(res)

except FileNotFoundError:
    print("filenotfounderror:file not exist")
except ZeroDivisionError:   
    print("ZeroDivisionError : can not divid by zero")
except Exception as err:
    print(f"error{err}")     
