# Q1- Enter your name and recive a greeting massage.
'''
name = input("Enter Your name\n")
greet = "\tGood Morning"
print(name+greet)   '''

# Q2- Write a letter and print it with name enterd by user.
'''
name = input("Enter your name\n")
date = input("Enter Date\n")

#latter =  ''' #Dear |<NAME>| , 
#Greeting form our team.
#congratulation.
#              You are selected .
#               Date:  |<DATE:>|'''

#latter=latter.replace('''|<NAME ,>|'''  , name)   #replace name and date in givrn string.
#latter=latter.replace('''|<DATE:>|''' , date)
#print (latter)   


#  detact a double space in string.
'''
st = "To  find  double spaces inside a string   other it    is present or  not"
#doublespace = st.find("  ")   #check and if present return first index.
replace =st.replace("  " , " ")
print(replace)
'''


# latter using escpae sequence.
st = 'Dear  Danish !,\nThis python course is nice \n \t\t\t Thanks!'
print(st)