class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        contents = self.file.read()
        books_list = contents.splitlines()
        print("-------------------------------------------")
        print("*****BOOKS*****")
        for book in books_list:
            book_info = book.split(',')
            print(f"Book Name: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of Pages: {book_info[3]}")
        print("-------------------------------------------")

    def add_book(self):
        title = input("Enter book title: ")
        if title != 'q':  
            author = input("Enter book author: ")
            if author != 'q':
                year = input("Enter first release year: ")
                if year != 'q':
                    pages = input("Enter number of pages: ")
                    if pages != 'q':
                        self.file.write(f"{title},{author},{year},{pages}\n")
                        self.file.flush()
                        print("-------------------------------------------")
                        print(f"Book Name: {title}, Author: {author}, Release Year: {year}, Number of Pages: {pages}")
                        print("Book added succesfuly")
                        print("-------------------------------------------")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book you want to remove: ")
        if title_to_remove != 'q':
            self.file.seek(0)
            books = self.file.readlines()
            found = False
        
            updated_books = [book for book in books if not book.startswith(title_to_remove + ',')]
        
            if len(updated_books) == len(books):
                print("Book not found.")
            else:
                self.file.seek(0)
                self.file.truncate()  
                self.file.writelines(updated_books)  
                self.file.flush()
                print("-------------------------------------------")
                print(f"The book '{title_to_remove}' has been removed successfully.")
                print("-------------------------------------------")

    def search_books(self, query, mode='title'):
        if query != 'q':
            self.file.seek(0)
            books = self.file.read().strip().splitlines()
            found_books = []
            print("-------------------------------------------")
            for book in books:
                book_info = book.split(",")
                if mode == 'title' and query.lower() in book_info[0].lower():
                    found_books.append(book)
                elif mode == 'author' and query.lower() in book_info[1].lower():
                    found_books.append(book)
                elif mode == 'year' and query == book_info[2]:
                    found_books.append(book)

            if not found_books:
                print(f"No books found with that {mode}.")
                return
        
            print("-------------------------------------------")
            print(f"Found books based on {mode}:")
            for book in found_books:
                book_info = book.split(",")
                print(f"Book Name: {book_info[0]}, Author: {book_info[1]}, Year: {book_info[2]}, Pages: {book_info[3]}")

    def update_book(self):
        print("-------------------------------------------")
        title_to_update = input("Enter the title of the book you want to update: ")
        if title_to_update != 'q':
            self.file.seek(0)
            books = self.file.readlines()
            found = False
            quit = False
            for i, book in enumerate(books):
                if book.startswith(title_to_update + ","):
                    found = True
                    print(f"Current book details: {book.strip()}")
                    new_title = input("Enter new book title: ")
                    if new_title == 'q':
                        quit = True
                        break
                    new_author = input("Enter new book author: ")
                    if new_author == 'q':
                        quit = True
                        break
                    new_year = input("Enter new first release year: ")
                    if new_year == 'q':
                        quit = True
                        break
                    new_pages = input("Enter new number of pages: ")
                    if new_pages == 'q':
                        quit = True
                        break
                    books[i] = f"{new_title},{new_author},{new_year},{new_pages}\n"
                    break
        
            if not found:
                print("Book not found.")
                return
            if not quit:
                self.file.seek(0)
                self.file.truncate()
                self.file.writelines(books)
                self.file.flush()
                print("-------------------------------------------")
                print("Book updated successfully.")
                print("-------------------------------------------")
                
lib = Library()

while True:
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Search by Title")
    print("5) Search by Author")
    print("6) Search by Year")
    print("7) Update Book")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("(You can input 'q' whenever you want if you quit!)")
    choice = input("Enter your choice: ")
    
    

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice in ['4', '5', '6']:
        print("-------------------------------------------")
        query = input(f"Enter the {'title' if choice == '4' else 'author' if choice == '5' else 'year'} to search: ")
        mode = 'title' if choice == '4' else 'author' if choice == '5' else 'year'
        lib.search_books(query, mode)
    elif choice == '7':
        lib.update_book()
    elif choice.lower() == 'q':
        del lib
        break
    else:
        print("Invalid choice. Please choose again.")
