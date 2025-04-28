#!/usr/bin/env python3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy import select, func, and_

# Set up SQLAlchemy core engine and metadata
engine = create_engine('sqlite:///bookstore.db')
metadata = MetaData()

# Define tables using SQLAlchemy Core (not ORM classes)
authors = Table('authors', metadata,
    Column('author_id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('country', String)
)

books = Table('books', metadata,
    Column('book_id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('author_id', Integer, ForeignKey('authors.author_id')),
    Column('year_published', Integer),
    Column('price', Float)
)

# Connect to the database
connection = engine.connect()

def basic_select():
    """Demonstrate a simple SELECT query using SQLAlchemy Core."""
    print("\n--- All Books ---")
    # Create a SELECT query
    query = select([books])
    
    # Execute the query
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"ID: {row['book_id']}, Title: {row['title']}, Year: {row['year_published']}, Price: ${row['price']}")

def filtering():
    """Demonstrate filtering with WHERE clause using SQLAlchemy Core."""
    print("\n--- Books published after 1950 ---")
    # Create a SELECT query with WHERE clause
    query = select([books.c.title, books.c.year_published])\
            .where(books.c.year_published > 1950)
    
    # Execute the query
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"Title: {row['title']}, Year: {row['year_published']}")

def join_example():
    """Demonstrate a JOIN operation using SQLAlchemy Core."""
    print("\n--- Books with Authors ---")
    # Create a SELECT query with JOIN
    query = select([books.c.title, authors.c.name.label('author'), books.c.year_published])\
            .select_from(books.join(authors))\
            .order_by(books.c.year_published)
    
    # Execute the query
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"'{row['title']}' by {row['author']} ({row['year_published']})")

def aggregation():
    """Demonstrate aggregation and GROUP BY using SQLAlchemy Core."""
    print("\n--- Books Count by Author ---")
    # Create a SELECT query with GROUP BY
    query = select([authors.c.name, func.count(books.c.book_id).label('book_count')])\
            .select_from(authors.outerjoin(books))\
            .group_by(authors.c.author_id)
    
    # Execute the query
    result = connection.execute(query)
    
    # Process results
    for row in result:
        print(f"Author: {row['name']}, Books: {row['book_count']}")

def advanced_query():
    """Demonstrate a more advanced query with multiple conditions using SQLAlchemy Core."""
    print("\n--- Books by UK authors published after 1950 ---")
    # Create a SELECT query with multiple conditions
    query = select([books.c.title, authors.c.name, books.c.year_published])\
            .select_from(books.join(authors))\
            .where(and_(
                authors.c.country == 'UK',
                books.c.year_published > 1950
            ))\
            .order_by(books.c.year_published)
    
    # Execute the query
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