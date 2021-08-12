# Dictionary is a collection of Key- value pairs.

myDictionary = {
    "FName": "Danish",
    "Lname": "Belal",
    "Class": "B.Tech(IT)",
    "Roll": "14",
    "Collage": "HNBGU",
    "Marks": [3, 4, 5, 6, 7],
    # We can creat a Dictionary inside a Dictionary.
    "Dict": {'name': 'Shahzeb', 'class': 'Diploma', "Dict2": {'name': 'Alam', 'class': 'electronnic'}}

}
'''
# print(myDictionary['FName'])
# print(myDictionary['Class'])
# print(myDictionary['Roll'])
print(myDictionary['Marks'])
myDictionary['Marks'] = [5, 6, 8, 8]  # we can chang key value os a Dictionary
print(myDictionary['Marks'])   # Vale of key[marks] will update by given value

# print(myDictionary['Dict']['name'])       # Calling a Dictionary value from dictionay MyDictionary
# print(myDictionary['Dict']['class'])
# print(myDictionary['Dict']['Dict2']['name'])  # calling value of Dict2, from Dict from MyDictionary
'''

 # Dictionary Methods

#print(myDictionary.keys())    #myDictionar.keys() will give all keys value. bydefault type is dict.key
#print(myDictionary.values())    # return all values of keys. 
#print(myDictionary.items())      # Prints the (key , values) for all contents of a Dictionary

#print(myDictionary)
updatedict = {           # Creating another dictionary to add insdie our oldest dict
    "Name":"arbaz",
    "class":"same"
}
#myDictionary.update(updatedict)    # push (updatdict) in (mydictionary).
#print(myDictionary)

print(myDictionary.get("Marks"))     # print value associate with key Marks.
print(myDictionary.get("Melo"))      # get() this will return none if key and its value is not present in dictionary.
print(myDictionary["Marks"])         #  this will thrown if Marks will  not present in dictionary.

# There are many more Dictionarys methods present in dictionay , if needed go google and search.