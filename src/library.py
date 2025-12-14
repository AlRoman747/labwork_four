from logging import exception


class Book:
    # книга, все данные о книге
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn


    def __repr__(self):
        return f'{self.title} {self.author} {self.year} {self.genre} {self.isbn}'




class BookCollection:
    def __init__(self):
        self._items = []

    def add(self, book: Book):
        self._items.append(book)

    def remove(self, book: Book):
        self._items.remove(book)

    def __getitem__(self, key):
        try:
            if isinstance(key, int):
                return self._items[key]

            if isinstance(key, slice):
                new_list = BookCollection()
                for item in self._items[key]:
                    new_list.add(item)
                return new_list
        except: raise IndexError("такой книги нет")
    def __iter__(self) -> list:
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)



class BookCatalog:
    def __init__(self):
        self._by_isbn = {}  # словарь по isbn
        self._by_author = {} # словарь по автору
        self._by_year = {} # словарь по году

    def add(self, book: Book):
        self._by_isbn[str(book.isbn)] = book
        self._by_year.setdefault(int(book.year), []).append(book)
        self._by_author.setdefault(str(book.author) , []).append(book)

    def remove(self, book: Book):
        # будем удалять, только если у книги правильный isbn, в других случаях даже не проверяем всё остальное
        try:
            del_book = self._by_isbn[book.isbn]
            del self._by_isbn[book.isbn]
            self._by_year[book.year].remove(del_book)
            self._by_author[book.author].remove(del_book)
        except: raise ValueError("Указан неправильный isbn книги для удаления")
    def get_by_isbn(self, isbn: str) -> Book:
        try: return self._by_isbn[str(isbn)]
        except: raise KeyError("Указан неправильный isbn книги")

    def get_by_author(self, author: str) -> list:
        try: return self._by_author[str(author)]
        except: raise KeyError("Указан неправильный автор книги")


    def get_by_year(self, year: int) -> list:
        try: return self._by_year[int(year)]
        except: raise KeyError("Указан неправильный год книги")



class Library:
    def __init__(self):
        self.BookCollection = BookCollection()
        self.IndexDict = BookCatalog()

    def search_by_isbn(self, isbn: str) -> Book:
        return self.IndexDict.get_by_isbn(isbn)
    def search_by_author(self, author: str) -> list:
        return self.IndexDict.get_by_author(author)
    def search_by_year(self, year: int) -> list:
        return self.IndexDict.get_by_year(year)

    

