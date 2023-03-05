class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.year}) - {book.genre}")

    def save_books(self, filename):
        try:
            with open(filename, 'w') as f:
                for book in self.books:
                    f.write(f"{book.title}|{book.author}|{book.genre}|{book.year}\n")
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_books(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    title, author, genre, year = line.strip().split('|')
                    book = Book(title, author, genre, year)
                    self.add_book(book)
        except Exception as e:
            print(f"Error loading file: {e}")

if __name__ == "__main__":
    library = Library()
    library.load_books("books.txt")
    library.list_books()
    library.save_books("books.txt")
