import os
import json

library = []
def save_library():
    with open('library.txt', 'w') as file:
        file.write(json.dumps(library, indent=4))

def load_library():
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            data = file.read()
            if data:
                global library
                library = json.loads(data)

def add_book():
    title = input("Enter the book title:")
    author = input("Enter the book author:")
    year = input("Enter the year of publication:")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'
    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read_status
    }
    library.append(book)
    print("Book added succesfully!")
    
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

def search_book():
    print("Search by /n1. Title /n2. Author /n3. genre /n4. year")
    choice = input("Enter your choice: ")
    query = input("Enter your search query: ")
    results = []
    if choice == '1':
        results = [book for book in library if book["title"].lower() == query.lower()]
    elif choice == '2':
        results = [book for book in library if book["author"].lower() == query.lower()]
    elif choice  == '3':
        results = [book for book in library if book["genre"].lower() == query.lower()]
    elif choice  == '4':
        results =[ book for book in library if book['year'].lower() == query.lower()]
    else:
        print("Invalid choice!")
        return
    if results:
        print("Matching available books:")
        for idx, book in enumerate(results, 1):
            read_status = "Read" if book["Read"] else "Unread"
            print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {read_status}")
    else:
        print("No matching books found!")


def display_all_books():
    if not library:
        print("Library is empty!")
    else:
        print("Your Library:")
        for idx, book in enumerate(library, 1):
            read_status = "Read" if book["Read"] else "Unread"
            print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {read_status}")
            
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        percentage_read = 0
    else:
        read_books = sum(1 for book in library if book["Read"])
        percentage_read = (read_books / total_books) * 100

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")
def main():
    load_library()
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_all_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

