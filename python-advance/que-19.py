# 19) Write a Python program to show method overloading

class math:
    def add(self,num1 = None,num2= None,num3 = None):
        if num1 != None and num2 != None and num3 != None :
            return num1 +num2 +num3
        elif num1 != None and num2 != None:
            return num1 + num2
        
obj = math()
print(obj.add(10,20,30)) 
print(obj.add(10,20)) 

class math2:
    def add1(self,*nums):
        total = 0
        for num in nums:
            total += num
        return total
        
obj2 = math2()
print(obj2.add1(10,20,30,40,50,60,70,80,90))        
