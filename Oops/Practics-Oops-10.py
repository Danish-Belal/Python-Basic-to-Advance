# Q1- create a class programmer for storing information of few programer working at Microsoft.
'''
class programmer:
    company = 'Microsoft'
    def GetDetail(self):
    #def GetDetail(self , Name , Post , salary , company):
        #print(f"Name {Name} {Post} {salary} {company}")
        print(f"Name: {self.Name} {self.Post} salary is: {self.salary} company:  {self.company}")



emp1 = programmer()
emp1.Name = 'Danish'
emp1.Post = 'CEO'
emp1.salary = 10000
emp1.company
emp1.GetDetail()
#emp1.GetDetail('Danish' , 'CEO' , 1000 ,  )


emp2 = programmer()
emp2.Name = 'Shahzeb'
emp2.Post = 'Chif'
emp2.salary = 1000
emp2.GetDetail()
#emp2.GetDetail(100 , 500 , 0)
'''


# Q2- Create a class calculator which is capble of finding square no , cube no , squareroot
'''
class Calculator:
    def __init__(self, num):
        self.Number = num

    def square(self):
        print(f'The square of {self.Number} is {self.Number **2}')

    def cube(self):
        print(f"The cube of {self.Number} is {self.Number **3}")

    def squareRoot(self):
        print(f"The squareroot of {self.Number} is {self.Number **0.5}")

a = int(input("Enter a no \n"))
a = Calculator(a)
a.square()
a.cube()
a.squareRoot()
'''

# Q3 - create a class attribute (a) and set (a) directly in object a=0 . Does not chng class attribute'.
# Q4 Greet user by Hello Massage. by using static Method.
'''

class Clc:
    a="Danish"

    @staticmethod
    def greet():
         print(f"***Hello! There ***  \n{num.a}")

num = Clc()
num.a='Belal'

print(Clc.a)           # if object attribute is create then class attribute will not change, only instance attribute will create
print(num.a)

Clc.a = 'Shahzeb'             # this will change class attributr
num.greet()
print(Clc.a)

'''

# Q-5 : A class Train , has method to book a ticket , get status(no of seat) and get fair information of train
#                                                                running under Indian Railway.
'''

class Train:
    def __init__(self, name,  fare, seat_information):
        self.name = name
        self.fare = fare
        self.seat_information = seat_information

    def trainName(self):
        print(f"The name of Train is {self.name} ")


    def getStatus(self):
        print(f"Total Available seat is {self.seat_information}")


    def fearInfo(self):
        print(f"Fear of Train is Rs.{self.fare} ")


    def ticketBooking(self):
        if (self.seat_information > 0):
            print(f"Your Ticket is booked. Ticket no is {self.seat_information}")
            self.seat_information = self.seat_information - 1
        else:
            print(f"Sorry! No seat available kindly try in Tatkal")

    def cancleTicket(self , seat_information):
        print(f"You have cancled your seat {seat_information}")
        self.seat_information = self.seat_information +1

Purva = Train('Purva-12303', 90, 2)
#Purva.trainName()
#Purva.getStatus()
#Purva.fearInfo()
Purva.ticketBooking()
Purva.getStatus()
Purva.ticketBooking()
Purva.cancleTicket(2)
Purva.ticketBooking()
Purva.getStatus()
Purva.ticketBooking()
'''
