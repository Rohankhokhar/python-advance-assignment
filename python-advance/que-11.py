# 11) Write a Python program to create a class and access the properties of the class using an object

class car:
    def __init__(self,company,color,model):
        self.company = company
        self.color = color
        self.model = model

    def display(self):
        print(f"company : {self.company} , color : {self.color} , model : {self.model}")


c1 = car("toyota","black",2025)
c1.display()