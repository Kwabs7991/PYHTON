import sys

#Object Oriented Project 002: Creating a Library Management System.
#Name: Kobbie Mike Tabi
#Date: 22/07/2020


class Library:
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books

    def displayAvailableBook(self):
        print("""\nThe books we have in our library: 
   ==============================================
   """)
        book_id = 0
        for book in self.list_of_books:
            book_id += 1
            print(f"{book_id}. {book}")

    def lend_book(self, requestedBook):
        if requestedBook in self.list_of_books:
            print("Yes, it has now been lended to you.")
            self.list_of_books.remove(requestedBook)
        else:
            print("No it is not in stock.")

    def add_book_back(self, returnedBook):
        self.list_of_books.append(returnedBook)
        print("Thanks for returning your borrowed book")


class Student:
    def request_book(self):
        print("Enter the name of the book you would like to check out:")
        self.book = input()
        return self.book

    def return_book(self):
        print("Enter the book you would like to return: ")
        self.book = input()
        return self.book


def main():
    library = Library([
        "The Last Battle", "The courage to be disliked",
        "Rich Dad's Guide to Investing", "I am not your Negro"
    ])

    student1 = Student()

    complete = False
    while complete == False:
        print("""\n\n ======= STUDENT LIBRARY MENU =======
  1.Display all available books.
  2. Student Requests a book.
  3. Student wants to return a book.
  4. Exit\n\n
        """)

        choice = int(input("Enter Choice: "))
        if choice == 1:
            library.displayAvailableBook(
            )  #Using the object "library", and then calling the method called "displayAvailableBook".
        elif choice == 2:
            library.lend_book(
                student1.request_book()
            )  #If we want to use the method lend_book then we are using the object "library", and then calling the method in the Student class called "request_book".
        elif choice == 3:
            library.add_book_back(
                student1.return_book()
            )  #If we want to use the method add_book_back then we are using the object "library", and then calling the method in the Student class called "return_book".
        elif choice == 4:
            sys.exit(
            )  # If we are suing this option we are exiting the program
        # else:
        #     print(int(input("Please correctly enter your choice: ")))


main()



""" 
Things to improve in future for this Project:

- Should add another method to show what books have been taken out.

- Make a dictionary (not siure if it would be in its own method) for the books in the library, so it has its book id and book name and that the book id/number does not change when we add it back in.

- Another method based on random generator to offer a "daily recommendation"

- Must have a student number before being able to take out a book (whether we do this before every request or at the start of the programm will be decided later)

- Method to seperate books into various categories.

- Method that restricts user to certain books dependent on their department.

"""
