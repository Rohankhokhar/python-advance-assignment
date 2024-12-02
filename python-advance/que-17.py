# 17) Write a Python program to show hybrid inheritance

class a():
    a = "i am class a"

class b(a):
    b = "i am class b"    

class c(a):
    c = "i am class c"

class d(c,b):
    d = "i am class d"

obj = d()

print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)