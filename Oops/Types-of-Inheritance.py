# Inheritance is a way to creating a new class from an existing class.
# Types of Inheritance.
# 1: Single Inheritance.
# 2: Multiple Inheritance
# 3: Multilevel inheritance

# 1: Single Inheritance --> Occurs , when child inheritance only a single parent class.

'''
class Employee:                     # base class / parent class
    company = 'Google'
    def detail(self):
        print("This is an Employee")


class Programmer(Employee):  # Programer class is interited by Employee(base) class . By single Parent class
    def getDetail(self):
        print("This is a Programmer")
    
    #company = 'Youtube'  .

e = Employee()
print(e.company)
e.detail()
p= Programmer()    
p.getDetail()
p.detail()    
print(p.company)
'''

# Multiple Inheritance. --> When child class inherited by  more than one  perent class.
'''
class Employee:                 # 1st Parent class
    company = 'Google'
    position = 'CEO'

class openSource():            # 2nd Parent class
    contribution = 'Opensource contributiion '
    level = 0
    def Codedetail(self):
        self.level = self.level+1
    position = "Head"

class Person(Employee , openSource):  # preson class is inheriting 2 parent class
    name = 'Danish'


p = Person()
p.Codedetail()    # Accessing openSource class
print(p.level)
p.Codedetail()
print(p.position)   #Accessing Employee class
print(p.contribution)

# Note: If we create same attribute in both parent class than Those attribute will consider whome class have first called. 
'''

# Multilevel Inheritance.  --> When a child class became parent class of other child class.
'''
class Employee:                 # 1st Parent class
    company = 'Google'
    position = 'CEO'

class openSource(Employee):            # 2nd Parent class
    contribution = 'Opensource contributiion '
    level = 0
    def Codedetail(self):
        self.level = self.level+1
    position = "Head"

class Person(openSource):  # preson(child) class is inheriting , parent class(openSource) which is inherited by (Employee) perent class
    Fname = 'Danish'

class Danish(Person):               # Danish is inherited by person , person is inherited by openSource , OpenSource is inherited by Employee
    Lname = 'Belal'



D = Danish()
print(D.Fname)            # Accsing Person class
print(D.Lname)           # Accsing Danish class
print(D.position)        # Accsing openSource class  Here we will get positoin is head because it is letest call and inherited by employee class.
print(D.company)         # # Accsing Employee class

'''

#























