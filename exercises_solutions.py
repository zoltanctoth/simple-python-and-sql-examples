#!/usr/bin/env python3
"""
SQL Exercises Solutions

This file contains the solutions to the exercises in exercises.py
"""

import sqlite3

def connect_db():
    """Connect to the bookstore database."""
    conn = sqlite3.connect('bookstore.db')
    conn.row_factory = sqlite3.Row
    return conn

# EXERCISE 1: Select all book titles and their prices
def exercise1():
    """
    Write a query to select all book titles and their prices.
    Sort the results by price in descending order.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "SELECT title, price FROM books ORDER BY price DESC"
    
    print("\nExercise 1: All book titles and prices (sorted by price)")
    cursor.execute(query)
    for book in cursor.fetchall():
        print(f"Title: {book['title']}, Price: ${book['price']}")
    
    conn.close()

# EXERCISE 2: Find books published in a specific decade
def exercise2():
    """
    Write a query to find all books published in the 1990s (1990-1999).
    Display the title and year published.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    query = """
    SELECT title, year_published 
    FROM books 
    WHERE year_published BETWEEN 1990 AND 1999
    ORDER BY year_published
    """
    
    print("\nExercise 2: Books published in the 1990s")
    cursor.execute(query)
    for book in cursor.fetchall():
        print(f"Title: {book['title']}, Year: {book['year_published']}")
    
    conn.close()

# EXERCISE 3: Find the average book price by author
def exercise3():
    """
    Write a query to calculate the average book price for each author.
    Display the author name and average price.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    query = """
    SELECT authors.name, AVG(books.price) as avg_price
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    GROUP BY authors.author_id
    ORDER BY avg_price DESC
    """
    
    print("\nExercise 3: Average book price by author")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"Author: {row['name']}, Average Price: ${row['avg_price']:.2f}")
    
    conn.close()

# EXERCISE 4: Find authors with more than one book
def exercise4():
    """
    Write a query to find authors who have written more than one book.
    Display the author name and the number of books they've written.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    query = """
    SELECT authors.name, COUNT(books.book_id) as book_count
    FROM authors
    JOIN books ON authors.author_id = books.author_id
    GROUP BY authors.author_id
    HAVING COUNT(books.book_id) > 1
    """
    
    print("\nExercise 4: Authors with more than one book")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"Author: {row['name']}, Books: {row['book_count']}")
    
    conn.close()

# EXERCISE 5: Find the oldest and newest book for each author
def exercise5():
    """
    Write a query to find the oldest and newest book for each author.
    Display the author name, oldest book title and year, and newest book title and year.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    query = """
    SELECT 
        a.name as author_name,
        (SELECT b1.title FROM books b1 WHERE b1.author_id = a.author_id ORDER BY b1.year_published ASC LIMIT 1) as oldest_book,
        (SELECT b2.year_published FROM books b2 WHERE b2.author_id = a.author_id ORDER BY b2.year_published ASC LIMIT 1) as oldest_year,
        (SELECT b3.title FROM books b3 WHERE b3.author_id = a.author_id ORDER BY b3.year_published DESC LIMIT 1) as newest_book,
        (SELECT b4.year_published FROM books b4 WHERE b4.author_id = a.author_id ORDER BY b4.year_published DESC LIMIT 1) as newest_year
    FROM authors a
    """
    
    print("\nExercise 5: Oldest and newest book for each author")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"Author: {row['author_name']}")
        print(f"  Oldest: '{row['oldest_book']}' ({row['oldest_year']})")
        print(f"  Newest: '{row['newest_book']}' ({row['newest_year']})")
    
    conn.close()

if __name__ == "__main__":
    print("SQL Exercises Solutions")
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5() 