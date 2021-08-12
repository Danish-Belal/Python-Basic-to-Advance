# Q1: create a dict of hindi words with values as their English Translation,
#  provided user with an option to look it up !
'''
MyDictionary = {
      "likhna": input("Englis word of likhna : "),
      "Khana":  input("Englis word of Khana : "),
      "Rona":   input("Englis word of Rona : "),
      "Hasna":   input("Englis word of Hasna : "),
      "jana":   input("Englis word of jana : ")

} 
print(MyDictionary)
 
# Direct acces value by giving key 
#print(MyDictionary["Hasna"])

# we can check options by seeing all keys.
#print( MyDictionary.keys())

#Acces dictinory by taking input from user. 
print(MyDictionary[input()]) 
'''



#Q2 : Enter 4 numbers and print unique numbers . we can do this by using propety of set.
'''
numbers = {int(input("Enter no1 :")) , int(input("Enter no2 :")),
           int(input("Enter no3 :")),int(input("Enter no4 :")),
           int(input("Enter no5 :")),int(input("Enter no5 :")),
           int(input("Enter no7 :")),int(input("Enter no8 :"))}

print(numbers) '''
 
 #Q3 , can int(18) and string(18) be added in a set
'''
s = { 18 , "18" , "18"}   #string and integer both can be print  in a set , both are unique
print(s)
'''


# Q4 find length.
'''
a = set()
a.add(20)
a.add(20.0)   #20.0 will consider as 20 and it will ignored cuz repeted element .
a.add("20")
print(len(a))
print(a)
'''
#Q5 type
'''
s= {}
print(type(s))   # this is Empty not set , this is empty directry
s set()          # This is Empty set
'''

# Q6 : Create a empty directry and allow your four friend to enter their fav langauge.
'''
Favlan= {}
subham=input("subham Enter your fav langauge\n ")
Shahzeb=input("Shahzeb Enter your fav langauge\n ")
Arbaz=input("Arbaz Enter your fav langauge\n ")
Motasim=input("Motasim Enter your fav langauge\n ")

Favlan['subham'] = subham
Favlan[' Shahzeb'] = Shahzeb
Favlan['Arbaz'] = Arbaz
Favlan['Motasim'] = Motasim
# if 2 langauge will same then both value will print
# but if 2 names will same then last updated value will be given to both.
print(Favlan)

'''

# Q9 can we chang the value insdie a list which is contained in srt

#s = { 2,5,7,"Danish" , [2,6]}    # list is unhashable so we cant add list in set.
s = {2,5,7,"Danish" , (2,6)}      # we can add tuple in set but we can not change tuple.cuz it is Hashable(fixed lifespan)
print(s)









