import json


class Library:

    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open("books.json", "r") as file:
                self.books = json.load(file) #converts JSON into python list

        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open("books.json", "w") as file:
            json.dump(self.books, file, indent=4)

    def show_books(self):
        if not self.books:
            print("\nNo books available in the library.")
            return
        
        print("\nAvailable Books:")
        for index, book in enumerate(self.books, start=1):
            status = "Available" if book["available"] else "Borrowed"
            print(f"{index}. {book['title']} - {status}")


    def add_book(self):
        
        title = input("\nEnter book title: ")

        new_book = {
            "title": title,
            "available": True
        }

        self.books.append(new_book)
        self.save_books()

        print(f"\nBook '{title}' added successfully!")


    def borrow_book(self):

        title = input("\nEnter book title to borrow: ")

        for book in self.books:

            if book["title"].lower() == title.lower():

                if not book["available"]:
                    print("\nSorry, this book is already borrowed.")
                    return

                book["available"] = False
                self.save_books()

                print(f"\nYou have successfully borrowed '{book['title']}'")
                return

        print("\nBook not found.")


    def return_book(self):

        title = input("\nEnter book title to return: ")

        for book in self.books:

            if book["title"].lower() == title.lower():

                if book["available"]:
                    print("\nThis book was not borrowed.")
                    return

                book["available"] = True
                self.save_books()

                print(f"\nYou have successfully returned '{book['title']}'")
                return

        print("\nBook not found.")

    def search_book(self):

        keyword = input("\nEnter book name to search: ").lower()

        found_books = []

        for book in self.books:

            if keyword in book["title"].lower():
                found_books.append(book)

        if not found_books:
            print("\nNo matching books found.")
            return

        print("\n===== Search Results =====")

        for index, book in enumerate(found_books, start=1):

            status = "Available" if book["available"] else "Borrowed"

            print(f"{index}. {book['title']} - {status}")
            

    def show_available_books(self):

        available_books = [book for book in self.books if book["available"]]

        if not available_books:
            print("\nNo available books right now.")
            return

        print("\n===== Available Books =====")

        for index, book in enumerate(available_books, start=1):
            print(f"{index}. {book['title']}")