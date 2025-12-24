import sqlite3


DB_NAME = "library.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_books():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("Animal Farm", "George Orwell", 1945, "Political satire", 112, 3),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 4),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 223, 7),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Dystopia", 256, 2),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Novel", 277, 3),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 6),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Novel", 281, 4),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopia", 311, 5),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic", 671, 2)
    ]

    cursor.executemany("""
    INSERT INTO books (
        name, author, publication_year, genre,
        number_of_pages, number_of_copies
    ) VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()


def get_all_books():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    conn.close()
    return books


def update_book_name(book_id, new_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE books
    SET name = ?
    WHERE id = ?
    """, (new_name, book_id))

    conn.commit()
    conn.close()


def delete_book(book_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    insert_books()

    print("📚 Все книги:")
    books = get_all_books()
    for book in books:
        print(book)

    print("\n✏ Изменяем название книги с id = 1")
    update_book_name(1, "Nineteen Eighty-Four")

    print("\n🗑 Удаляем книгу с id = 2")
    delete_book(2)

    print("\n📚 Книги после изменений:")
    books = get_all_books()
    for book in books:
        print(book)
