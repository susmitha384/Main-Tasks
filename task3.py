 # Main library dictionary 

library = {} 
# Function to add a new book 

def add_book(): 

    book_id = int(input("Enter Book ID: ")) 

    if book_id in library: 

        print("Book ID already exists!\n") 

        return 


    title = input("Enter book title: ") 

    author = input("Enter author name: ") 

    year = int(input("Enter publication year: ")) 

    available = True 
    library[book_id] = { 

        "title": title, 

        "author": author, 

        "year": year, 

        "available": available 

    } 

    print("Book added successfully!\n") 
# Function to remove a book 

def remove_book(): 

    book_id = int(input("Enter Book ID to remove: ")) 
    if book_id in library: 

        del library[book_id] 

        print("Book removed successfully!\n") 

    else: 

        print("Book not found!\n") 
# Function to search books 

def search_book(): 

    keyword = input("Enter title or author to search: ").lower() 

    found = False 
    for book_id in library: 

        book = library[book_id] 

        if keyword in book["title"].lower() or keyword in book["author"].lower(): 

            print(f"\nBook ID: {book_id}") 

            print(book) 

            found = True 
    if not found: 

        print("No matching books found.\n") 
# Function to update book information 

def update_book(): 

    book_id = int(input("Enter Book ID to update: ")) 

    if book_id not in library: 

        print("Book not found!\n") 

        return 
    book = library[book_id] 

    print("Leave blank to keep current value.") 

    title = input(f"New title ({book['title']}): ") 

    author = input(f"New author ({book['author']}): ") 

    year = input(f"New year ({book['year']}): ") 

    if title: 

        book["title"] = title 

    if author: 

        book["author"] = author 

    if year: 

        book["year"] = int(year) 

    print("Book updated successfully!\n") 
# Function to generate report 

def library_report(): 

    print("\n--- Library Report ---") 
    for book_id in library: 
        book = library[book_id] 
        print(f"ID: {book_id} | {book}") 

    print() 
# Function to calculate statistics 

def library_statistics(): 

    total = len(library) 
    available = 0 
    for book_id in library: 

        if library[book_id]["available"]: 

            available += 1 

    print("\n--- Library Statistics ---") 

    print("Total books:", total) 

    print("Available books:", available) 

    print("Borrowed books:", total - available) 

    print() 
# Menu-driven program 

while True: 

    print("1. Add Book") 

    print("2. Remove Book") 

    print("3. Search Book") 

    print("4. Update Book") 

    print("5. Library Report") 

    print("6. Library Statistics") 

    print("7. Exit") 

    choice = input("Enter your choice: ") 

    if choice == "1": 
        add_book() 

    elif choice == "2": 
        remove_book() 

    elif choice == "3": 
        search_book() 

    elif choice == "4": 
        update_book() 

    elif choice == "5": 
        library_report() 

    elif choice == "6": 
        library_statistics() 

    elif choice == "7": 
        print("Exiting Library System...") 

        break 

    else: 
        print("Invalid choice! Try again.\n") 