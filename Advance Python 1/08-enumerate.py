# Enumerate function adds counter to an iterable and returns it.

list1 = ['Danish' , 5 , 8.9 ,  True]
'''
index = 0
for i in list1:
    print(i ,index)
    index +=1
'''

for index , item in enumerate(list1):
    print(index , item) 





