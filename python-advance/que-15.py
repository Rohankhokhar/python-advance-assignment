# 15) Write a Python program to show multiple inheritance.

class a():
    a = "i am class a"

class b():
    b = "i am class b"

class c(a,b):
    c = "i am class c"   

obj = c()

print(obj.a)
print(obj.b)
print(obj.c)         