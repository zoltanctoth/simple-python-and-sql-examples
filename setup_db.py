#!/usr/bin/env python3
import sqlite3
import os

# Create database file
def setup_database():
    # Delete the database file if it exists
    if os.path.exists('bookstore.db'):
        os.remove('bookstore.db')
    
    # Connect to the database (this will create it if it doesn't exist)
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE authors (
        author_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        country TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE books (
        book_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER,
        year_published INTEGER,
        price REAL,
        FOREIGN KEY (author_id) REFERENCES authors (author_id)
    )
    ''')
    
    # Insert example data for authors
    authors = [
        (1, 'J.K. Rowling', 'UK'),
        (2, 'George Orwell', 'UK'),
        (3, 'Harper Lee', 'USA'),
        (4, 'Jane Austen', 'UK')
    ]
    
    cursor.executemany('INSERT INTO authors VALUES (?, ?, ?)', authors)
    
    # Insert example data for books
    books = [
        (1, 'Harry Potter and the Philosopher\'s Stone', 1, 1997, 15.99),
        (2, '1984', 2, 1949, 12.50),
        (3, 'To Kill a Mockingbird', 3, 1960, 14.75),
        (4, 'Pride and Prejudice', 4, 1813, 9.99),
        (5, 'Harry Potter and the Chamber of Secrets', 1, 1998, 16.99),
        (6, 'Animal Farm', 2, 1945, 11.25)
    ]
    
    cursor.executemany('INSERT INTO books VALUES (?, ?, ?, ?, ?)', books)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database 'bookstore.db' created successfully with example data!")

if __name__ == "__main__":
    setup_database() 