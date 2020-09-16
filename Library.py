class Library:

    User_history = {}

    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        for i in book_list:
            self.User_history[i] = None

    def add_book(self, book_name):
        self.book_list.append(book_name)
        self.User_history.update({book_name: None})

    def lend_book(self, name, book):
        if self.User_history[book] is not None:
            print("This book is Already Borrowed by", self.User_history[book])
            return 0
        self.User_history.update({book: name})

    def display_books(self):
        print(self.book_list)
        print(self.User_history)

    def return_books(self, book_name):
        try:
            if self.User_history[book_name] is not None:
                print("Returned Successfully!!!")
                self.User_history.update({book_name: None})

            else:
                print("There is no book by this name which had been borrowed")
        except:
            print("There is no book by this name which had been borrowed")

Shoumik = Library(["Wings of Fire", "Rich dad Poor dad", "The Alchemist"], "Shoumik_Library")

while True:
    print("What do you wanna do?")
    print("Press 0 to exit()")
    print("Press 1 for Add Books")
    print("Press 2 for Lend Books")
    print("Press 3 for Display Books")
    print("Press 4 for Return Books")
    menu = int(input("Enter a number: "))

    if menu == 0:
        break
    elif menu == 1:
        bName = input("Enter Book Name: ")
        Shoumik.add_book(bName)
    elif menu == 2:
        lName = input("Enter the name: ")
        book = input("Enter the name of the Book: ")
        Shoumik.lend_book(lName, book)
    elif menu == 3:
        Shoumik.display_books()
    elif menu == 4:
        rName = input("Enter the Book name you wanna Return: ")
        Shoumik.return_books(rName)
