#!/usr/bin/env python3
import sqlite3

def connect_db():
    """Connect to the bookstore database."""
    conn = sqlite3.connect('bookstore.db')
    # Configure connection to return rows as dictionaries
    conn.row_factory = sqlite3.Row
    return conn

def basic_select():
    """Demonstrate a simple SELECT query."""
    conn = connect_db()
    cursor = conn.cursor()
    
    print("\n--- All Books ---")
    cursor.execute("SELECT * FROM books")
    for book in cursor.fetchall():
        print(f"ID: {book['book_id']}, Title: {book['title']}, Year: {book['year_published']}, Price: ${book['price']}")
    
    conn.close()

def filtering():
    """Demonstrate filtering with WHERE clause."""
    conn = connect_db()
    cursor = conn.cursor()
    
    print("\n--- Books published after 1950 ---")
    cursor.execute("SELECT title, year_published FROM books WHERE year_published > 1950")
    for book in cursor.fetchall():
        print(f"Title: {book['title']}, Year: {book['year_published']}")
    
    conn.close()

def join_example():
    """Demonstrate a JOIN operation."""
    conn = connect_db()
    cursor = conn.cursor()
    
    print("\n--- Books with Authors ---")
    cursor.execute("""
    SELECT books.title, authors.name as author, books.year_published
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    ORDER BY books.year_published
    """)
    
    for record in cursor.fetchall():
        print(f"'{record['title']}' by {record['author']} ({record['year_published']})")
    
    conn.close()

def aggregation():
    """Demonstrate aggregation and GROUP BY."""
    conn = connect_db()
    cursor = conn.cursor()
    
    print("\n--- Books Count by Author ---")
    cursor.execute("""
    SELECT authors.name, COUNT(books.book_id) as book_count
    FROM authors
    LEFT JOIN books ON authors.author_id = books.author_id
    GROUP BY authors.author_id
    """)
    
    for record in cursor.fetchall():
        print(f"Author: {record['name']}, Books: {record['book_count']}")
    
    conn.close()

def advanced_query():
    """Demonstrate a more advanced query with multiple conditions."""
    conn = connect_db()
    cursor = conn.cursor()
    
    print("\n--- Books by UK authors published after 1950 ---")
    cursor.execute("""
    SELECT books.title, authors.name, books.year_published
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    WHERE authors.country = 'UK' AND books.year_published > 1950
    ORDER BY books.year_published
    """)
    
    for record in cursor.fetchall():
        print(f"'{record['title']}' by {record['name']} ({record['year_published']})")
    
    conn.close()

if __name__ == "__main__":
    # Run all example queries
    basic_select()
    filtering()
    join_example()
    aggregation()
    advanced_query() 