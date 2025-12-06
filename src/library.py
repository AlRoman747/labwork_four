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

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._items[key]

        if isinstance(key, slice):
            # срез → возвращаем *новый BookList* на тех же объектах
            new_list = BookCollection()
            for item in self._items[key]:
                new_list.add(item)
            return new_list

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)


