from library import Library

library = Library()

while True:

    print("\n==============================")
    print("      LIBRARY SYSTEM")
    print("==============================")
    print("1. Show All Books")
    print("2. Show Available Books")
    print("3. Add Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Search Book")
    print("7. Exit")
    print("==============================")

    choice = input("Enter choice: ")

    if choice == "1":
        library.show_books()

    elif choice == "2":
        library.show_available_books()

    elif choice == "3":
        library.add_book()

    elif choice == "4":
        library.borrow_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.search_book()

    elif choice == "7":
        print("\nExiting system... Goodbye!")
        break

    else:
        print("\nInvalid choice! Try again.")