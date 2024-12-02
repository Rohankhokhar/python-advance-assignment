# 4) Write a Python program to create a file and print the string into the file.

file = "example2.txt"
f1 = open(file,'w')
f1.write("hello world 2")
f1.close()