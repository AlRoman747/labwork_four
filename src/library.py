import os
import requests
from dotenv import load_dotenv


class Book:
    # книга, все данные о книге
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        self.content = None

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
        except KeyError: raise KeyError("KeyError. The book doesn't exist.")
        except ValueError: raise ValueError("ValueError. The book doesn't exist.")
        except TypeError: raise TypeError("TypeError. The book doesn't exist.")
        except Exception: raise "The book doesn't exist."
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
        except: raise ValueError("incorrect book's isbn for delete")

    def get_by_isbn(self, isbn: str) -> Book:
        try: return self._by_isbn[str(isbn)]
        except: raise KeyError("incorrect book's isbn")

    def get_by_author(self, author: str) -> list:
        try: return self._by_author[str(author)]
        except: raise KeyError("incorrect book's author")


    def get_by_year(self, year: int) -> list:
        try: return self._by_year[int(year)]
        except: raise KeyError("incorrect book's year")



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

class GenerateBook:
    def __init__(self, book: Book):
        self.book = book

    def build_book(self):
        load_dotenv()

        CATALOG_ID = os.getenv("YC_CATALOG_ID")
        API_KEY = os.getenv("YC_API_KEY")
        MODEL = "yandexgpt-lite"  # Используемая модель

        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {API_KEY}"
        }

        # Текст промта для модели
        prompt_data = {
            "modelUri": f"gpt://{CATALOG_ID}/{MODEL}",
            "completionOptions": {
                "stream": False,
                "temperature": 0.7,
                "maxTokens": "1000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": f"You are a master of literary stylization. Your task is to write in the style of {self.book.author}. \
                            In the style of the {self.book.year}s. Use techniques from the {self.book.genre} genre."
                },
                {
                    "role": "user",
                    "text": f"{self.book.title}"
                }
            ]
        }

        return url, headers, prompt_data

class GetWrittenBook:
    def __init__(self, url, headers, prompt_data):
        self.url = url; self.headers = headers; self.prompt_data = prompt_data
    def book_to_read(self):
        try:
            response = requests.post(self.url, headers=self.headers, json=self.prompt_data)
            response.raise_for_status()  # Проверка на ошибки HTTP

            result = response.json()
            # Извлечение сгенерированного текста из ответа
            generated_text = result["result"]["alternatives"][0]["message"]["text"]

            return generated_text

        except Exception as e:
            raise ValueError(f"Error with generate: {e}")

