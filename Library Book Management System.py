
class Book:
    def __init__(self, title, author, year, isbn, pages):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.isbn}, Pages: {self.pages}"


library = []

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the year of publication: "))
    isbn = input("Enter the ISBN: ")
    pages = int(input("Enter the number of pages: "))
    book = Book(title, author, year, isbn, pages)
    library.append(book)
    print("Book added successfully!")

def display_books():
    if library:
        print("\nBooks in the Library:")
        for book in library:
            print(book)
    else:
        print("\nThe library is empty!")

def search_book():
    search_title = input("Enter the title to search for: ")
    found_books = [book for book in library if search_title.lower() in book.title.lower()]
    if found_books:
        print("\nSearch Results:")
        for book in found_books:
            print(book)
    else:
        print("No books found with that title!")


def main():
    while True:
        print("\nLibrary Book Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by Title")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
