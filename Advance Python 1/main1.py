# we use when we want to use or import our some module/function in other file.
# but not all function then we use ( __name__ == "__main__") . if we import this file in other file then only those 
# function will execute who will not written under ( __name__ == "__main__").

def greet(name):
    print(f"Good Day! {name}")


#print(__name__)
'''
if __name__ == "__main__":            # code in this will not execute in other file. check this in main2.py
    n = input("Enter your Name: ")
    greet(n)
'''

greet("Danish")   # greet and this function will execute in main2.py file
