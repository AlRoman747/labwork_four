class Book:
    # книга, все данные о книге
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn


class BookCollection:
    def __int__(self):
        self._items: list[Book] = []

    def add(self, book: Book):
        self._items.append(book)

    def remove(self, book: Book):
        self._items.remove(book)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._items[key]

        if isinstance(key, slice):
            new_list = BookCollection()
            for item in self._items[key]:
                new_list.add(item)
            return new_list

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)



class BookCatalog:
    def __init__(self):
        self._by_isbn: dict[str, Book] = {}  # словарь по isbn
        self._by_author: dict[str, list[Book]] = {} # словарь по автору
        self._by_year: dict[int, list[Book]] = {} # словарь по году

    def add(self, book: Book):
        self._by_isbn[book.isbn] = book
        self._by_year.setdefault(book.year, []).append(book)
        self._by_author.setdefault(book.author, []).append(book)

    def remove(self, book: Book):
        # будем удалять, только если у книги правильный isbn, в других случаях даже не проверяем всё остальное
        if book.isbn in self._by_isbn.keys():
            del_book = self._by_isbn[book.isbn]
            del self._by_isbn[book.isbn]
            if book.year in self._by_year.keys(): self._by_year[book.year].remove(del_book)
            else: raise ValueError("Указан неправильный год книги для удаления")
            if book.author in self._by_author.keys(): self._by_author[book.author].remove(del_book)
            else: raise ValueError("Указан неправильный автор книги для удаления")
        else: raise ValueError("Указан неправильный isbn книги для удаления")
    def get_by_isbn(self, isbn: str) -> Book:
        if isbn in self._by_isbn.keys(): return self._by_isbn.get(isbn)
        raise ValueError("Указан неправильный isbn книги")

    def get_by_author(self, author: str) -> list:
        if author in self._by_author.keys(): return self._by_author.get(author, [])
        raise ValueError("Указан неправильный автор книги")


    def get_by_year(self, year: int) -> list:
        if year in self._by_year.keys(): return self._by_year.get(year, [])
        raise ValueError("Указан неправильный год книги")



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



