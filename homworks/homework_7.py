import sqlite3


connect = sqlite3.connect("books.db")
cursor = connect.cursor()
def create_table():
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute('''CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    publication INTEGER NOT NULL,
    genre TEXT NOT NULL,
    number_of_pages INTEGER NOT NULL,
    number_of_copies INTEGER NOT NULL)  ''')
def insert_book():
    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 15),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopia", 288, 10),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Science Fiction", 256, 12),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 20),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 450, 25),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic", 671, 8),
        ("War and Peace", "Leo Tolstoy", 1869, "Classic", 1225, 5),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 14),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 281, 11),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Classic", 277, 9)
    ]
    cursor.executemany(
        '''
        INSERT INTO books(name,author,publication,genre,number_of_pages,number_of_copies)
        
        VALUES(?,?,?,?,?,?)''',

        books
    )
    connect.commit()
if __name__ == "__main__":
    create_table()
    insert_book()