
# Use open function to read then content of sample.txt file
'''
#f = open("sample.txt", 'r')   # Program to open a file , r stands for reading mode
f = open("sample.txt")         # if we dont specify the mode then it will take read mode . 
#data = f.read()
#data = f.read(12)    # this will only read 10 character

#other methos to read a file
data = f.readlines()   # f.readline() use to read a line and f.readlines() use to read all lines
print(data)
f.close()
'''

# Write a file.
'''
#f= open('sample.txt', 'w')  #'w' stands for write mode and 
f= open('sample.txt', 'a')   # a stand for append mode. if given file name is not present it will create a file
data = f.write("\n I am Appending")

f.close()
'''

# with Statment.
# with statment used for automatically  close
#in read mode
'''
with open('sample.txt' , 'r') as f:
    a=f.read()
print(a)  
'''

# In write mode
with open('sample.txt', 'w') as f:
    a=f.write('Hello World')
print(a)    













