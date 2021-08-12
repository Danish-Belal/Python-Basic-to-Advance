
class Employee:
    # Creating class Attribute
    company = 'Google'
    salery = 100                # Preference of instance attribute will high if it will present 

Danish = Employee()
Shahzeb = Employee()
Danish.salery = 300                 # Instance Attribute --> It Belongs to Objects
Shahzeb.salery = 400

print(Danish.company)
print(Shahzeb.company)

Shahzeb.company = "You-Tube"        # We can change a class Attribute.

print(Danish.company)
print(Shahzeb.company)              # Shahzeb Company attribute will change 
print(Danish.salery)
print(Shahzeb.salery)