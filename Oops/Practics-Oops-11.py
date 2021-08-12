# Q1 Create a 3d vector using 2d vector.
'''
class C2dvec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}k"


class C3dvec(C2dvec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j+ {self.kcap}k"


vec2 = C2dvec(1, 3)
vec3 = C3dvec(1, 9, 7)
print(vec2)
print(vec3)
'''

# Q2- create a class pet form class aminal and further create a class dog form pet . Add method  bark to class Dog
'''
class Animal:
    print("Animals Are good.")

class Pet(Animal):
    print("This is a Pet")

class Dog(Pet):

    @staticmethod
    def bark():
        print("Dog is Barking")


Tommy = Dog()
Tommy.bark()

'''

# Q3 - use setter and getter to chang attribute of a class employee
'''
class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return (self.salary*self.increment)


    @salaryAfterIncrement.setter  
    def salaryAfterIncrement(self , inc):
        self.increment = inc /self.salary



e= Employee()        
print(e.salaryAfterIncrement)
print(e.increment)

e.salaryAfterIncrement = 2000
print(e.salaryAfterIncrement)
print(e.salary)
print(e.increment)

'''

# Q4- Create a complex class to write a equation of complex no. Overloding + and * Operator
# Multiplication of complex no --> (a+bi)(c+di) = (ac-bd) + (ad+bc)i
'''
class complex:
    def __init__(self , r , i):
        self.real = r
        self.imagnery = i

    def __add__(self , m):          # Uploading + operators
        return complex(self.real+ m.real , self.imagnery+m.imagnery)    

    def __mul__(self , m):              # uploading * operators
        mulReal =(self.real*m.real - self.imagnery*m.imagnery) 
        mulImg = (self.real*m.imagnery + self.imagnery*m.real) 
        return complex(mulReal , mulImg)      
    
    def __str__(self):
        if self.imagnery<0:
            return f"{self.real} - {-self.imagnery}i"
        else:
            return f"{self.real} + {self.imagnery}i"

n1 = complex(1, -4)
n2 = complex(331 , -37)
print( n1+n2)
print(n1*n2)

'''


# Q5 - Write a __str__() method to print the vector as 7i^ + 8j^ + 10k^ a three dimention vector. find length of list
'''
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

    def __len__(self):
        return len(self.vec)
 
v1 = Vector([1, 4, 6 ])
v2 = Vector([1, 6, 9])

print(v1)
print(v2)

print(len(v1))
print(len(v2))
'''
# upload + and * OPerator in vector. And find length.

class Vector:
    def __init__(self , vec):
        self.vec = vec 

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index +=1
        return str1[:-1]  

    def __add__(self , vec2):
        newList=[]
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)    

    def __mul__(self , vec2):
        sum = 0
        for i in range(len(self.vec)):
           sum += self.vec[1]*vec2.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)

v1 = Vector([2,3 ,7])
v2 = Vector([3,6,8])  
print(v1+v2) 
print(v1*v2)
print(len(v1))
print(len(v2))












