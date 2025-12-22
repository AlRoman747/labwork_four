from src.library import *
import random

def generate_book() -> Book:
    authors = [
        "George Orwell", "J.K. Rowling", "Stephen King", "Agatha Christie", "Haruki Murakami",
        "Gabriel García Márquez", "Ernest Hemingway", "Jane Austen", "Fyodor Dostoevsky",
        "Leo Tolstoy", "Franz Kafka", "Toni Morrison", "Chinua Achebe", "Virginia Woolf",
        "Mark Twain", "Charles Dickens", "J.R.R. Tolkien", "Ray Bradbury", "Maya Angelou",
        "Isaac Asimov", "Margaret Atwood", "Kurt Vonnegut", "Neil Gaiman", "Brandon Sanderson",
        "Ursula K. Le Guin"
    ]

    titles = [
        "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice", "The Catcher in the Rye",
        "The Lord of the Rings", "Harry Potter and the Philosopher's Stone", "The Hobbit", "Animal Farm",
        "Brave New World", "The Chronicles of Narnia", "The Da Vinci Code", "The Hunger Games", "The Alchemist",
        "The Little Prince", "The Kite Runner", "Gone with the Wind", "War and Peace", "Crime and Punishment",
        "Moby-Dick", "Wuthering Heights", "Jane Eyre", "Frankenstein", "Dracula", "The Odyssey", "The Divine Comedy",
        "Don Quixote", "Les Misérables", "The Count of Monte Cristo", "The Picture of Dorian Gray",
        "The Brothers Karamazov",
        "Anna Karenina", "One Hundred Years of Solitude", "Ulysses", "Catch-22", "Slaughterhouse-Five", "Beloved",
        "The Handmaid's Tale", "The Road", "Dune", "The Name of the Rose", "The Shining", "It",
        "A Song of Ice and Fire",
        "The Girl with the Dragon Tattoo", "The Silent Patient", "Where the Crawdads Sing", "Educated",
        "Sapiens: A Brief History of Humankind", "Thinking, Fast and Slow"
    ]

    genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Thriller", "Romance", "Horror",
              "Historical Fiction", "Biography", "Autobiography", "Memoir", "Self-Help", "Science", "History"]


    return Book(titles[random.randint(0, len(titles) - 1)],
                authors[random.randint(0, len(authors) - 1)],
                random.randint(0, 2025),
                genres[random.randint(0, len(genres) - 1)],
                f'{random.randint(100, 999)}-{random.randint(0, 9)}-{random.randint(10000, 99999)}-{random.randint(100, 999)}-{random.randint(0, 9)}')

book_list = BookCollection()
book_dict = BookCatalog()
library = Library()
authors, years, isbns = set(), set(), set()

def start_book():
    """начинаем сразу с 5 книг, если выпадет 5 удалений"""
    for _ in range(5):
        book = generate_book()
        book_list.add(book)
        book_dict.add(book)
        authors.add(str(book.author)); years.add(int(book.year)); isbns.add(str(book.isbn))



def functions(book, removed_book):
    """возвращает словарь команд
    словарь вынесен в отделбную функцию чтобы какждый раз работать с новой книгой"""
    return {    "add": (book_list.add, book_dict.add, book),
                "remove": (book_list.remove, book_dict.remove, removed_book),
                "search_by_isbn": book_dict.get_by_isbn,
                "search_by_year": book_dict.get_by_year,
                "search_by_author": book_dict.get_by_author,
                "get_with_error_list": (book_list.__getitem__, book_list.__len__()),
                "get_with_error_dict": (book_dict.get_by_isbn, "")
    }
start_book()
# print(*book_list, sep='\n')
def get_commands(n):
    for i in range(1, n+1):
        book = generate_book()
        removed_book = random.choice(book_list)
        random_command = random.choice(list(functions(book, removed_book).keys()))
        func = functions(book, removed_book)[random_command]

        if random_command == "add":
            print(f"случайное событие №{i} - добавление книги: {book.__repr__()}")
            func[0](func[-1])
            func[1](func[-1])
            authors.add(book.author); years.add(book.year); isbns.add(book.isbn)
        elif random_command == "remove":
            print(f"случайное событие №{i} - удаление книги: {removed_book.__repr__()}")
            func[0](func[-1])
            func[1](func[-1])
            authors.discard(removed_book.author); years.discard(removed_book.year); isbns.discard(removed_book.isbn)

        elif random_command == "search_by_isbn":
            rand_isbn = random.choice(list(isbns))
            print(f"случайное событие №{i} - поиск книги по isbn: {rand_isbn}")
            print(func(rand_isbn))
        elif random_command == "search_by_year":
            rand_year = random.choice(list(years))
            print(f"случайное событие №{i} - поиск книг за этот год: {rand_year}")
            print(func(rand_year))
        elif random_command == "search_by_author":
            rand_author = random.choice(list(authors))
            print(f"случайное событие №{i} - поиск книг этого автора: {rand_author}")
            print(func(rand_author))

        elif random_command == "get_with_error_list":
            print(f"случайное событие №{i} - поиск книги с ошибкой")
            try: func[0](func[-1])
            except Exception as e: print(e)
        elif random_command == "get_with_error_dict":
            print(f"случайное событие №{i} - поиск книги по isbn с ошибкой")
            try: func[0](func[-1])
            except Exception as e: print(e)