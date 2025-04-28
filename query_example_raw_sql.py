#!/usr/bin/env python3
from sqlalchemy import create_engine

# Create connection to the SQLite database
engine = create_engine('sqlite:///bookstore.db')
connection = engine.connect()

def basic_select():
    """Demonstrate a simple SELECT query using raw SQL."""
    print("\n--- All Books ---")
    
    # Execute raw SQL query
    query = "SELECT * FROM books"
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"ID: {row['book_id']}, Title: {row['title']}, Year: {row['year_published']}, Price: ${row['price']}")

def filtering():
    """Demonstrate filtering with WHERE clause using raw SQL."""
    print("\n--- Books published after 1950 ---")
    
    # Execute raw SQL query with WHERE clause
    query = "SELECT title, year_published FROM books WHERE year_published > 1950"
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"Title: {row['title']}, Year: {row['year_published']}")

def join_example():
    """Demonstrate a JOIN operation using raw SQL."""
    print("\n--- Books with Authors ---")
    
    # Execute raw SQL query with JOIN
    query = """
    SELECT books.title, authors.name as author, books.year_published
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    ORDER BY books.year_published
    """
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"'{row['title']}' by {row['author']} ({row['year_published']})")

def aggregation():
    """Demonstrate aggregation and GROUP BY using raw SQL."""
    print("\n--- Books Count by Author ---")
    
    # Execute raw SQL query with GROUP BY
    query = """
    SELECT authors.name, COUNT(books.book_id) as book_count
    FROM authors
    LEFT JOIN books ON authors.author_id = books.author_id
    GROUP BY authors.author_id
    """
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"Author: {row['name']}, Books: {row['book_count']}")

def advanced_query():
    """Demonstrate a more advanced query with multiple conditions using raw SQL."""
    print("\n--- Books by UK authors published after 1950 ---")
    
    # Execute raw SQL query with multiple conditions
    query = """
    SELECT books.title, authors.name, books.year_published
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    WHERE authors.country = 'UK' AND books.year_published > 1950
    ORDER BY books.year_published
    """
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"'{row['title']}' by {row['name']} ({row['year_published']})")

if __name__ == "__main__":
    # Run all example queries
    basic_select()
    filtering()
    join_example()
    aggregation()
    advanced_query()
    
    # Close connection
    connection.close() 