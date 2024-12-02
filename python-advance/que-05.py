# 5) Write a Python program to read a file and print the data on the console

file = "example2.txt"

f1 = open(file,'r')
data = f1.read()
print(data)
f1.close()