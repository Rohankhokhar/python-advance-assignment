# 6) Write a Python program to check the current position of the file cursor using tell().

file = "example.txt"

f1 = open(file,'r')
print(f"cursor position : {f1.tell()}") #tell method use to find what cursor position in file
data = f1.read(5)
print(f"data : {data}")
print(f"after cursor position : {f1.tell()}")
f1.close()