# Sets in Python are collection of non repetitave Element.
'''
a = { 1 ,2 ,4 , 5 , 1}   # sets ignore repatitave Element.
print(type(a))
print(a)

b = {}             # this is the wrong way to declare empty set.
print(type(b))     # this is a Empty Dictinory type not empty set.
print(b)
'''


# Initilizing And Empty set and adding value in empty set.
c = set()           # to initilize empty set , set() will be an empty set.
#print(type(c))
# Adding Valur in empty set.
c.add(4)
c.add(3)
c.add(5)
c.add(5)                           # will not add repeted element in set.
c.add(8)
# c.add([1,3,5])                    # we cant add List to set.
# c.add((2,9,1,8))                   # But we can add tuple to set.
# c.add(({"name":"Danish"}))        # We can not add Dictionary to set.
print(c)

# Note : if our Data is not Hashable(fixed lifespan ) then we can't add that to set. like list , Disctinory etc.
# but tuples are fixed element we cant further add more value in list so we can add this in set.

#print(len(c))                   # len() will gives the length of set .
#c.remove(5)                      # remove() will remove 5 from set.
#c.remove(15)                     # if element is not present it will thrown error that not present in set.
#print(c)

#print(c.pop())                  # pop() will remove a ramdom element and return poped element.
#print(c)

#print(c.clear())                # Empities the set . 
#print(c)                        # after clear we will get an empty set.

#print(c.union({3,5,7}))          # Union value will add in set.
 
#print(c.intersection({5,8,9,1}))   # Intersection will return common element in both set.

d = {5,8,9,1}                        # if we want we can create a set for intersection/ union.
print(c.intersection(d))

