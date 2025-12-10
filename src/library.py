class Book:
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

    def get_by_isbn(self, isbn: str) -> Book:
        return self._by_isbn.get(isbn)

    def get_by_author(self, author: str) -> list:
        return self._by_author.get(author, [])

    def get_by_year(self, year: int) -> list:
        return self._by_year.get(year, [])
