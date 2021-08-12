# The method name with propety is called getter method.
#(function+@name.setter) is setter decorator

class BankBalance:
    name = 'Danish'
    Amount = 10000
    intrest = 500
    #totalAmount = 10500
  
    @property               # propety decorator is also known as getter.
    def totalAmount(self):
        return self.Amount+self.intrest


    @totalAmount.setter      # Setter method.
    def totalAmount(self, value):   # setter used to set value, here we set value of totalAmount.
        self.intrest = value - self.Amount

e = BankBalance()
print(e.totalAmount)        # propety decorator is used like attribute , 
e.totalAmount = 15000         # if we want to chng value then we will used setter method.
print(e.totalAmount)
print(e.Amount)
print(e.intrest)





