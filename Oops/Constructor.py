# Constructor is a special method which is first run as soon as the object created.
# it takes self arguent and can also take further argument.


class Employee:
    company = 'Microsoft'

    # We can pass more than one argument in a constructor.
    #def __init__(self):
    def __init__(self , name , salary , id):        # We can use multiple attributes in constructor.
        print("Constructor is created")
        print(f"Name is: {name} \nsalary is: {salary}  \n Id is: {id} ")

    def detail(self, signature, lastname):
        print(
            f"Name of empoyee is  {lastname} salary is   \n signature is {signature}")

    @staticmethod
    def time():
        print("The time is 9.30 PM")

    @staticmethod
    def greet():
        print("Thanks!")


Danish = Employee('Danish' , 100000 , 14)           

'''
Danish.name = 'Danish'
Danish.salary = 1000
Danish.detail('@danish' , 'Belal')
Danish.time()
Danish.greet()
'''














