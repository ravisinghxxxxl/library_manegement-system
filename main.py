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
                f"You have been issued {bookName}. Please keep it safe and return it within 90 days")
            self.books.remove(bookName)
        else:
            print("Sorry! this book already has been issued to someone else. Please wait untill it has been returned")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book, Hope you enjoyed it")


class student:
    pass


if __name__ == "__main__":
    centralLibrary = Library(
        ["Algorithams", "Data structures", "The C language", "Python"])
    centralLibrary.displayAvailableBooks()
    centralLibrary.borrowBook("Python")
    centralLibrary.displayAvailableBooks()
    centralLibrary.returnBook("Python")