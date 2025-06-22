class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Livre '{book.title}' ajouté à la bibliothèque."

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return f"Livre '{book_title}' supprimé de la bibliothèque."
        return f"Livre '{book_title}' non trouvé."

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                return f"Livre '{book_title}' emprunté."
        return f"Livre '{book_title}' non disponible."

    def return_book(self, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                return f"Livre '{book_title}' rendu."
        return f"Livre '{book_title}' non trouvé dans les livres empruntés."

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        return [book.title for book in self.borrowed_books]

"""
if __name__ == "__main__":
    library = Library()

    library.add_book(Book("Le Petit Prince", "Antoine de Saint-Exupéry", 2034))
    print("livre dispo apres ajout du Petit Prince :", library.available_books())

    library.add_book(Book("1984", "George Orwell", 345))
    print("Livres disponibles après ajout de 1984 :", library.available_books())

    library.borrow_book("Le Petit Prince")
    print("Livres disponibles après emprunt du Petit Prince :", library.available_books())
#   library.borrow_book("Le Petit Prince")
    print(" la liste des livres emprunter:",library.borrowed_books_list())
    #   library.return_book("Le Petit Prince")
    print("Livres disponibles après retour du Petit Prince :", library.available_books())

"""