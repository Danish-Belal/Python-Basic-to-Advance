
# name = "Danis"
# print(name)
# Accesing string form index 1 to last. last no will not be included.
#print(name[1: 8])
# print(name[:6])       # Acces black with minimum index. as same as name[0:6]
# print(name[1:])       # Acces blank with maximum length. as same as name [1:6]
# print(name[-6 :  -1])  # this will print Danis ,    as same as name[0:4]

name = "DanishisagoodBoy"
# print(name[0 : :3])           # [0: ] will give string and [:3] will skip 2 digit and print only third.

# print(len(name))              #len(name) will give the length of name integer.

# print(name.endswith("Boy"))   #string.endswith("Boy") will check string is ending with these strings , return trur or false

# print(name.startswith("D"))   #string.startswith("D") which check , string start with given value or not.

#print(name.count("is"))          # string.count("is"), will count total occurence of a char or substring in string.

#print(name.capitalize())          # capitalize , become capital  first latter of given string.

#print(name.find("B"))             # find() , find a char or word present in a string or not , if true return index , else return -1

print(name.replace( "o" , "hello"))   #ewplace( o , hello ) will replay o with i from entire string.

