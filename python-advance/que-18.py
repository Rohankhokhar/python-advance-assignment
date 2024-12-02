# 18) Write a Python program to demonstrate the use of super() in inheritance

class math1:
    def info(self):
        return "i am parent class"
    
class math2(math1):
    def info(self):
        print(super().info())
        return "i am child class"

obj = math2()
print(obj.info())    
