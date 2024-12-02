# 16) Write a Python program to show hierarchical inheritance. 

class a():
    a = "i am class a"

class b1(a):
    b1 = "i am class b1"    

class b2(a):
    b2 = "i am class b2"

class c1(b1):
    c1 = "i am class c1"

class c2(b1):
    c2 = "i am class c2"

obj = c2()

print(obj.a)
print(obj.b1)
print(obj.c2)