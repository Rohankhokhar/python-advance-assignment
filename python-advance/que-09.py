# 9) Write a Python program to handle file exceptions and use the finally block for closing the file.

try :
    file_name = input("enter existing file name:")
    f1 = open(file_name,'r')
    data = f1.read()
    print(data)

except FileNotFoundError:
    print("filenotfounderror:file not exist")
except Exception as err:
    print(f"error{err}") 
finally :
    print("excute complated and now close ")