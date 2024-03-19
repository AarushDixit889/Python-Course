# Inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

class Driver(Person):
    def __init__(self,name,age,smart_driver):
        super().__init__(name,age)
        self.smartDriver=smart_driver
    def getIsSmartDriver(self):
        return self.smartDriver

Driver("Aarush",8,True)

# A -> B -> C -> Added