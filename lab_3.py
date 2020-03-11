import sys
class Library:
    def _init_(self, AllBooks):
        self.availBooks = AllBooks

    def getAvailableBooks(self):
        print("Books Which are currently Available:")
        for book in self.availBooks:
            print(book)

    def RequestBook(self,BookRequest):
        if BookRequest in self.availBooks:
            print("The Book has been Granted,u have duration of 1 month for renewal/return")
            self.availBooks.remove(BookRequest)
        else:
            print("Sorry for inconvenience the book requested is currently unavailable.")

    def ReturnOrRenewalBook(self, Book,s):
        if(s=="return"):
            self.availBooks.append(Book)
            print("Thanks for return!")
        else:
            print("Another one month of renewal has been done for the "+Book)

class Student:
    def _init_(self,StudentList,Listid):
        self.StudentList = StudentList
        self.ListId=Listid
    def raiseBookRequest(self):
        print("Enter the name of the book")
        self.book = input()
        return self.book

    def BookReturn(self):
        print("Enter the name of the returning Book")
        self.book = input()
        return self.book
    def BookRenewal(self):
        print("Enter the name of the renewal Book")
        self.book = input()
        return self.book
class Faculty:
    def _init_(self, listoffaculty,Listid):
        self.listoffaculty = listoffaculty
        self.ListIdFac=Listid
def main():
    library = Library(["Harry Potter", "Games Of Thrones", "Fifty Shades","I too had a love story"])
    faculty = Faculty(["Shanks","Monkey D Garp"],["AdvanceHaki","The Fist"])
    student = Student(['Luffy',"Rajesh"],["PirateKing","Haki"])
    Name = input("enter name or id")
    if (Name in  student.StudentList or Name in faculty.listoffaculty) or (name in ListId or name in ListIdFac):
        print("You are authorized to access!")
    else:
        print("You are not access to use facilities of library :")
        sys.exit()
    done = False
    while done == False:
        print(""" LIBRARY Management System
                  1. Display  available books
                  2. Request a book
                  3. Return a book
                  4. Renewal a book
                  5. Exit
                  """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            library.getAvailableBooks()
        elif choice == 2:
            library.RequestBook(student.raiseBookRequest())
        elif choice == 3:
            bookname = input("Enter the book to return ")
            if bookname in library.availBooks:
                print(" You are returning the wrong Book !. Please Enter the correct Book ")
            else:
                library.ReturnOrRenewalBook(bookname,"return")
        elif choice==4:
            bookname = input("Enter the book to renewal ")
            library.ReturnOrRenewalBook(bookname,"renewal")
        elif choice == 5:
            sys.exit()
main()