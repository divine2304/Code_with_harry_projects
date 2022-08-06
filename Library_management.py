#LIBRARY MANAGEMENT SYSTEM FOR BOOKS:

from datetime import datetime
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

class Librabry:
    def __init__(self,library_name,list_of_books):
        self.library_name=library_name
        self.list_of_books=list_of_books
        self.lender_names={}

        for books in self.list_of_books:
            self.lender_names[books]=None


    def display_books(self):
        for books in self.list_of_books:
            print(books)

    def lend_book(self,book,reader):
        if book in self.list_of_books:
            if self.lender_names[book] is None:
                self.lender_names[book]=reader
                print("Book lent successfully!",timestampStr)
            else:
                print(f"Sorry can't lend this book because book is lent to: {self.lender_names[book]}")
        else:
            print("You have entered WRONG book name!")

    def return_book(self,book,reader):
        if book in self.list_of_books:
            if self.lender_names[book] is not None:
                self.lender_names.pop(book)
                print("Returned successfully!",timestampStr)
            else:
                print("Book is not lent to anyone!")
        else:
            print("You have entered WRONG book name!")

    def add_book(self,bookname):
        self.list_of_books.append(bookname)
        self.lender_names[bookname]=None
        print("Added successfully!",timestampStr)

    def delete_book(self,bookname):
        self.list_of_books.remove(bookname)
        self.lender_names.pop(bookname)
        print("Deleted successfully!",timestampStr)

if __name__ == "__main__":

    try:
        list_books=["Eleven minutes", "The great gatsby", "perks of being wallflower", "The alchemist", "Eternal sinner", "How to think like a monk", "Subtle art of not giving a *uck", "5 feet apart", "Half girlfriend\n"]
        library_name="NERD's"
        Nerd=Librabry(library_name, list_books)
        print( f"welcome to {Nerd.library_name} LIBRARY\n press: d for Displaying books.\n l for Lending books.\n r for returning book.\n a to add book.\n b to delete book.\n and x to exit.")


        Exit=False
        while(Exit != True):
            inp=input("\nYour Option:")

            if inp=="d":
                Nerd.display_books()
                print("List is as above on ",timestampStr)

            elif inp=="l":
                inp2=input("Your name:".lower())
                inp3=input("Books name:".lower())
                Nerd.lend_book(inp3,inp2)


            elif inp=="r":
                inp2 = input("Your name:".lower())
                inp3 = input("Books name:".lower())
                Nerd.return_book(inp3, inp2)


            elif inp== "a" :
                inp3=input("Book name:".lower())
                Nerd.add_book(inp3)


            elif inp=="b":
                inp3=input("Book name:".lower())
                Nerd.delete_book(inp3)

            elif inp=="x":
                Exit=True
                break

            else:
                continue

    except Exception as e:
        print("Something went wrong. Please check. !!!")



