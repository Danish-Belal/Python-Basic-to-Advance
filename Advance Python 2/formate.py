# formate method were using when f"string" was not introduced , there are still code which has not change in fstring.

name = "Danish"
study = "B.tech"
roll =  14

#print(f" Name is {name} , class is {study} Roll is {roll}")  #using f'string' 

a = "Name is {}, class is {} , Roll is{}".format(name, study , roll)   # using formate 
print(a)

a = "Name is {2}, class is {0} , Roll is{1}".format(name, study , roll) # we can use index value first roll, name, study
print(a)