class Library:
    
    def __init__(self, listofBooks):
        self.Books = listofBooks

    def AvailableBook(self):
        print("Books in our Library are: ")
        for books in self.Books:
            print("* "+books)

    def borrowBook(self , bookName):
        if bookName  in self.Books:
            print(f"You have been issued {bookName} Book. Kindly return it within 15 Days. ")
            self.Books.remove(bookName)
            return True
        
        elif bookName is " ":
            print("Please Enter a Valid Book Name")
            return False

        elif bookName not in self.Books:
            print(f"This Book is not in our Library")
            return False

        else:
            print(f"Sorry! {bookName} Book has been issued. Kindly wait till return.")
            return False    

    def returnBook(self, bookName):
        if bookName not in self.Books:
            print("Sorry this Book does not belong to our Library.")
            print("If You want to can donate this book to our library. 😀")
        else:    
            self.Books.append(bookName)        
            print("Thanks for returning this Book. We hope Book was useful for you.\n**Visit Again**")

    def donateBook(self,bookName):
        self.Books.append(bookName)
        print(f"Thanks for Donating {bookName}  Book to our Library. We hope this will useful for others.")


class Student:
    def requestBook(self):
        self.book= input("Enter the name of you want to borrow: ")
        return self.book

    def returntBook(self):
        self.book= input("Enter the name of you want to Return: ")
        return self.book 

    def donateBook(self):
        self.book = input("Enter The name of the Book you want to Donate: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["DataStructure" , "Algorithm" , "Java" , "Python" , "OS"])
    #centralLibrary.AvailableBook()
    student = Student()

    while(True):
        welcomeMsg = '''
        *** Welcome in Central Library.***
        Please Choose an Option.
        1: List of Books.
        2: Request for a Book.
        3: Return Book.
        4: Donate a Book.
        5: Exit.    '''

        print(welcomeMsg)
        a = int(input("Enter Your choice: "))
        if a == 1:
            centralLibrary.AvailableBook()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returntBook())

        elif a== 4:
            centralLibrary.donateBook(student.donateBook())

        elif a ==5:
            print("** Thanks for visiting Central Library. Visit Again. **") 
            exit()       






