from src.simulation import *
import pytest

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



def rand_book(seed):
    book = generate_book()
    return book
def test_book_author():
    book = rand_book(748)
    assert book.author in authors

def test_book_year():
    book = rand_book(748)
    assert book.year in range(0, 2026)


def test_book_genre():
    book = rand_book(748)
    assert book.genre in genres


def test_book_title():
    book = rand_book(748)
    assert book.title in titles

def test_book_remove_and_add():
    book = rand_book(748)
    rm_book = rand_book(748)
    lst = BookCollection()
    dct = BookCatalog
    lst.add(book)
    lst.add(rm_book)
    assert len(lst) == 2
    lst.remove(rm_book)
    assert len(lst) == 1

