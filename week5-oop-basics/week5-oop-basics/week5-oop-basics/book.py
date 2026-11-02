class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def borrow_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
            print("Book borrowed successfully!")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        self.status = "Available"
        print("Book returned successfully!")

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", self.status)


book1 = Book("Python Basics", "John")
book1.display_info()
book1.borrow_book()
book1.display_info()
