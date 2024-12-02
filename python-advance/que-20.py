# 20) Write a Python program to show method overriding.

class animal:
    def sound(self):
        return "animal sound"
    
class dog(animal):
    def sound(self):
        return "dog is bhaw bhaw" 

class cat(animal):
    def sound(self):
        return "cat is meaow meaow"

dog1 = dog()
cat2 = cat()

print(dog1.sound())
print(cat2.sound())