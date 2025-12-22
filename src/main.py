from src.simulation import *


def main() -> None:
    print(f"Welcome to console library\nIf you wanna leave the library, write -1\nBut, if you wanna get into the world of fictional books, write your favorite author")
    move = input()
    if move == '-1': print("see you soon")

    while move != '-1':
        print(f"Good choice\nLets move on and choose one of these action, what you can do here\nWrite only number of action")
        print(f"1. start random simulation\n"
              f"2. create your own book\n"
              f"3. see the random shelf of books\n"
              f"4. read random book")
        try:
            action = int(input())
            if action == 1:
                print("write how many actions in simulation you want")
                steps = int(input())
                get_commands(steps)
            elif action == 2:
                print("write author of book, title, genre and in what year this book wrote")
                author, title, genre, year = input(), input(), input(), int(input())
                book = Book(title, author, year, genre,f'{random.randint(100, 999)}-{random.randint(0, 9)}-{random.randint(10000, 99999)}-{random.randint(100, 999)}-{random.randint(0, 9)}')
                print(f'book {book} added on shelf')
            elif action == 3:
                shelf = book_list
                print(*shelf.__iter__(), sep='\n')
            elif action == 4:
                book = generate_book()
                print(f"rn you will read {book.title} by {book.author} in genre: {book.genre}, what was wrote in {book.year}")
                try:
                    generator = GenerateBook(book)
                    url, headers, prompt_data = generator.build_book()

                    # сгенерированный текст
                    writer = GetWrittenBook(url, headers, prompt_data)
                    generated_text = writer.book_to_read()

                    print("=" * 50)
                    print(generated_text)

                    # Сохранение в файл
                    with open(f"{book.title}.txt", "w", encoding="utf-8") as f:
                        f.write(f"{book.title} by {book.author} in genre: {book.genre}; {book.year} year\n")
                        f.write(generated_text)

                except Exception as e:
                    print(f"error: {e}")

            else:
                print("print num from 1 to 4")


        except Exception as e:
            if "invalid literal for int() with base 10:" in str(e): print("write only number")
        print("Do u wanna continue? If not, just type -1")
        move = input()
    print("thanks for visit library! see you soon")

if __name__ == "__main__":
    main()


