#!/usr/bin/env python3
"""
SQL Exercises for Workshop Participants

Instructions:
1. Complete each function with the appropriate SQL query
2. Run the file to test your solutions
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
    
    # TODO: Write your query here
    # query = ""
    
    print("\nExercise 1: All book titles and prices (sorted by price)")
    # Uncomment the code below when you've written your query
    # cursor.execute(query)
    # for book in cursor.fetchall():
    #     print(f"Title: {book['title']}, Price: ${book['price']}")
    
    conn.close()

# EXERCISE 2: Find books published in a specific decade
def exercise2():
    """
    Write a query to find all books published in the 1990s (1990-1999).
    Display the title and year published.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    # TODO: Write your query here
    # query = ""
    
    print("\nExercise 2: Books published in the 1990s")
    # Uncomment the code below when you've written your query
    # cursor.execute(query)
    # for book in cursor.fetchall():
    #     print(f"Title: {book['title']}, Year: {book['year_published']}")
    
    conn.close()

# EXERCISE 3: Find the average book price by author
def exercise3():
    """
    Write a query to calculate the average book price for each author.
    Display the author name and average price.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    # TODO: Write your query here
    # query = ""
    
    print("\nExercise 3: Average book price by author")
    # Uncomment the code below when you've written your query
    # cursor.execute(query)
    # for row in cursor.fetchall():
    #     print(f"Author: {row['name']}, Average Price: ${row['avg_price']:.2f}")
    
    conn.close()

# EXERCISE 4: Find authors with more than one book
def exercise4():
    """
    Write a query to find authors who have written more than one book.
    Display the author name and the number of books they've written.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    # TODO: Write your query here
    # query = ""
    
    print("\nExercise 4: Authors with more than one book")
    # Uncomment the code below when you've written your query
    # cursor.execute(query)
    # for row in cursor.fetchall():
    #     print(f"Author: {row['name']}, Books: {row['book_count']}")
    
    conn.close()

# EXERCISE 5: Find the oldest and newest book for each author
def exercise5():
    """
    Write a query to find the oldest and newest book for each author.
    Display the author name, oldest book title and year, and newest book title and year.
    (This is more challenging and may require multiple queries or subqueries)
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    # TODO: Write your query here (this one is tricky!)
    # query = ""
    
    print("\nExercise 5: Oldest and newest book for each author")
    # You'll need to implement your own solution here
    
    conn.close()

if __name__ == "__main__":
    print("SQL Exercises - Complete the functions in this file")
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    
    print("\nSolutions are available in exercises_solutions.py") 