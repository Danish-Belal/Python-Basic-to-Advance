# Q1 a program to find grestest no among four no enterd by user.
'''
a = int(input("Enter no 1 "))
b = int(input("Enter no 2 "))
c = int(input("Enter no 3 "))
d = int(input("Enter no 4 "))
'''
'''
if (a>b and a>c and a>d):
    print(a ,"a is greater")
elif(b>a and b>c and b>d):
    print(b , "b is greater")    
elif(c>a and c>b and c>d):
    print(c ,"c is greater")
else:
    print(d, "d is greater")         


# another method
if (a>d):
    f1=a
else:
    f1=d
if(b>c):
    f2=b
else:
    f2=c     
if(f1>f2):
    print(f1 , " is greater")
else:
    print(f2 , " is Greater")
'''


# studend pass or not in 3 sub enterd by user.
'''
sub1= int(input("Enter marks in sub1\n"))
sub2= int(input("Enter marks in sub2\n"))
sub3= int(input("Enter marks in sub3\n"))

outof = int(input("Marks out of "))
tno = 3*outof
tmarks = sub1+sub2+sub3

percent = (100*tmarks)/tno
print(percent ,"%")
if(sub1<33 or sub2<33 or sub3<33):
    print("You failed due to less than 33 marks in sub")
elif (percent==45):
    print("You are passed")
elif (percent>90):
    print("You passed with excillent") 
elif(percent>70 and percent<90 ):    
    print("You passed with star marks")
else:
    print("Work haed Dude ! you failes.")       
'''

#   check the following text , if given string are present then spam or not.
'''
text = input("Enter your text.\n")
spam = False
if ("make a lot money" in text):
    spam = True
elif("click on this" in text):
    spam = True
elif("Suscribe here" in text):
    spam = True
elif("Buy now" in text):
    spam = True

if(spam):
    print("This is a spam")
else:
    print("This is good  and not spam.")
'''


# Q4: input user name contains less than 10 char or not.
'''
username= input("Enter your name\n")
if(len(username)<10):
    print("Your name have less than 10 character")
else:
    print("Your name have more than 10 char")        
'''

# Q5: To check wether a given name is present in a list or not.
'''
l = ["Danish" , "Shahzeb" , "Arbaz" , "Motasim"]
if(input() in l):                                   # in will check  that given input is present in list or not.
        print("Name is present in list.")
else:
    print("Name is not present in list.")    
'''


# to check where the conversition is about Danish or not.
 
conv= input("Enter is conversation\n")
if ("Danish" in conv):
    print("The conversation is about Danish.")
else:
    print("The conversation is not about Danish.")     


