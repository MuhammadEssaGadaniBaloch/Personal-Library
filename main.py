book_list = list()

# Menu items
menu = """ 
1) Add Book
2) Remove Book 
3) View Books
4) Press E to Exit 
"""

# Add books
def add_book(booklist, book):
    booklist.append(book)
    print("Book added successfully")

# Remove books
def remove_book(booklist, book):
    if book in booklist:
        booklist.remove(book)
        print("Book removed successfully")
    else:
        print("Book not found in the list")

# Display all books
def display_list(booklist):
    if booklist:
        print("Added Books ->", ", ".join(booklist))
    else: 
        print("No books in the list.")

# Exit Program
def exit_program():
    print("Thank you for visiting the book library system.")
    exit()  # Terminates the program

# Main program loop
while True:
    print(menu)
    choice = input("Your Choice: ").strip().lower()

    if choice == "1":  # Add books
        book_name = input("Enter the book name you want to add: ")
        add_book(book_list, book_name)

    elif choice == "2":  # Remove book
        book_name = input("Enter the book name to remove: ")
        remove_book(book_list, book_name)

    elif choice == "3":  # View book list
        display_list(book_list)

    elif choice == "e":  # Exit program
        exit_program()

    else:
        print("Invalid entry")
        input("Press Enter to return to the main menu!")
