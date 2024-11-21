class Book:
    def __init__(self,title,pages,author,price):
        self._title=title
        self._pages=pages
        self._author=author
        self._price=price
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_pages(self):
        return self._pages
    def get_price(self):
        return self._price           
    def book_length(self):
        if self._pages>200:
            print('The book is long.')
    def update_title(self, new_title):
        old_title = self.get_title()
        self._title = new_title
        print(f"Book title updated from '{old_title}' to '{self.get_title()}'")

    def update_author(self, new_author):
        old_author = self.get_author()
        self._author = new_author
        print(f"Author updated from '{old_author}' to '{self.get_author()}'")
class Ebook(Book):
    def __init__(self, title, pages, author, price):
        super().__init__(title, pages, author, price)
    def description(self):
        print(f'{self.get_title()} is an ebook.')
class PaperBackBook(Book):
    def __init__(self, title, pages, author, price):
        super().__init__(title, pages, author, price)
    def description(self):
        print(f'{self.get_title()} is a paperback book.')        


book1=Ebook('Tom n Jerry',300,'Me',1000)
print(book1.get_title())
print(book1.get_pages())
print(book1.get_author())
print(book1.get_price())
book1.description()




