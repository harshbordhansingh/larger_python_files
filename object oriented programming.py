class Dog:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        print(name)
        print(age)
    '''def __add__(self, x):
        return x+1
    def bark(self):
        print("bark")
d.bark()
print(d.__add__(5))
print(type(d))'''


d = Dog("Tim", 32)
d2 = Dog("Bill", 31)