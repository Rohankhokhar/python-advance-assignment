#  14) Write a Python program to show multilevel inheritance.

class a():
    a = "i am a"

class b(a):
    b = "i am b"

class c(b):
    c = "i am c"

obj = c()
print(obj.a)
print(obj.b)
print(obj.c)