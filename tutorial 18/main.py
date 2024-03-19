class Person:
    def __init__(self,name,gender,ischild):
        self.name=name
        self.gender=gender
        self.ischild=ischild
    def getName(self):return self.name
    def getGender(self):return self.gender
    def getChild(self):return self.ischild
person1=Person("aarush","male",True)

print("Details of person")
print("Name is "+person1.getName())
print("Gender is "+person1.getGender())
print("Child is "+str(person1.getChild()))

