# super method is used to access the method of a super class in drived class.

class Employee:
    company = 'Google'
    position = 'CEO'

    def em(self):
        print("I am a employee in Google")


class openSource(Employee):

    def em(self):
        super().em()
        print("I aslo do open source contribution")

class Person(openSource):
    def em(self):
        super().em()
        print("I am a good person too")
    

class Danish(Person):   
    def em(self):
        super().em()
        print("My name is Danish")


e = Employee()
e.em()

o = openSource()
o.em()

p = Person()
p.em()

d = Danish()
d.em()



# if we want to access a method from a super/base class then we use super methed.   ***super().method/constructor-name()***
