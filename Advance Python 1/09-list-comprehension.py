# list comprehension is an elegant way to creats list based on exesting list
# We can use this one liner comprehensioner for dictnory ans sets also.

#l1 = [3,5,6,7,8,90,12,34,67,0]
'''
# For addind even in l2
l2 =[]
for item in l1:
    if item%2 == 0:
        l2.append(item)
print(l2)
'''
'''
# Shortcut to write the same:
l2 = [item for item in l1 if item < 8]
l3 = [item for item in l1 if item%2 ==0]   # creating a list for 
print(l2)
print(l3)
'''

# print a reaptated element from both list.

l4 = ['am' , 'em' , 'fcgh' , 'em' , 'em']
l5 = ['am', 'f' , 'em' , 'rg' , 'em']
flist = [item for item in  l4+l5 if item == 'em']
#print(flist)
#print(flist.count('em'))

a= [4,6,8,5,4,4,4]
b = [4,5,6,4,5,4]
c = [i for i in a+b if i==4]
print(c)
print(c.count(4))