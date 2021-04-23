class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print("* " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please keep it safe and return it within 90 days\n")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry! this book already not availiable or has been issued to someone else. Please wait untill book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book, Hope you enjoyed it")


class student:

    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to add/return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(
        ["Algorithams", "Data structures", "The C language", "1984", "Python"])
    student = student()
    while(True):
        welcomeMsg = '''
        === Welcome to central library ==
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for using central library. Have a great day!")
            exit()
        else:
            print("Invalid choice!")
