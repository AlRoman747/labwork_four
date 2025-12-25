# Laboratory Work No. 4: OOP Library

## Introduction
The OOP-based **Library** project provides functionality for generating random book-related events, adding books to shelves, and generating random books using AI.

## How to Run
First, create a `.env` file and a `texts` directory in the project root. This is required for text generation.

In the `.env` file, add your **API key** and your **agent ID** from **Yandex Cloud**. Without these credentials, text generation will not work.

All generated texts will be stored in the `texts` directory.

In future versions, it is planned to add support for generating texts by selected authors, with custom titles, genres, and time-based stylistic settings.

---

## Project Structure



 <pre>
├── src/
│   ├── .env                          # API keys for the neural network
│   ├── library.py                    # Implementation of all core classes
│   ├── main.py                       # Entry point for running the library via CLI
│   ├── simulation.py                 # Random book generation logic
│   └── __init__.py
│
├── tests/
│   ├── rand_generate.py              # Generation of various data arrays
│   ├── sorting_test.py               # Sorting algorithm tests
│   ├── stack_test.py                 # Stack functionality tests
│   └── __init__.py
│
├── pyproject.toml
├── .pre-commit-config.yaml
├── .gitignore
└── README.md                         # Project description

</pre>


---

## BookCollection Class
- `__getitem__` — retrieves one element (by index) or multiple elements (by slice)
- `__iter__` — iterator support
- `__len__` — returns the collection size
- `add / remove` — methods for adding and removing items

---

## BookCatalog Class
- `add / remove` — methods for adding and removing books
- `get_by_isbn / author / year` — retrieves book(s) by ISBN, author, or publication year

---

## Library Class
Provides search functionality based on specified parameters.

---

## GenerateBook and GetWrittenBook Classes
Responsible for generating and retrieving AI-generated book content using **Yandex GPT**.

Both classes inherit from `BaseLLMClients`.

---

## BaseLLMClients Class
Encapsulates shared infrastructure responsibilities and defines a unified API interaction contract.

Common behavior such as request URLs and headers is centralized in this class.

---

## Additional Information
The `src` directory contains the implementation files required to complete the laboratory assignment.

The library operates entirely via the command line interface. Users must follow terminal instructions and enter the required numeric options.

When writing a custom book, each parameter must be entered on a new line.

The `tests` directory contains **Pytest** test cases used to validate the functionality of the application and its individual components.

Your simaulation in n.1 had seed

