#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Set up SQLAlchemy basics
Base = declarative_base()
engine = create_engine('sqlite:///bookstore.db')

# Define models that map to our database tables
class Author(Base):
    __tablename__ = 'authors'
    
    author_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String)
    
    # Define relationship to books
    books = relationship("Book", back_populates="author")
    
    def __repr__(self):
        return f"<Author(name='{self.name}', country='{self.country}')>"

class Book(Base):
    __tablename__ = 'books'
    
    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    year_published = Column(Integer)
    price = Column(Float)
    
    # Define relationship to author
    author = relationship("Author", back_populates="books")
    
    def __repr__(self):
        return f"<Book(title='{self.title}', year_published={self.year_published}, price=${self.price})>"

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def basic_select():
    """Demonstrate a simple SELECT query using SQLAlchemy."""
    print("\n--- All Books ---")
    books = session.query(Book).all()
    for book in books:
        print(f"ID: {book.book_id}, Title: {book.title}, Year: {book.year_published}, Price: ${book.price}")

def filtering():
    """Demonstrate filtering with WHERE clause using SQLAlchemy."""
    print("\n--- Books published after 1950 ---")
    books = session.query(Book.title, Book.year_published).filter(Book.year_published > 1950).all()
    for book in books:
        print(f"Title: {book.title}, Year: {book.year_published}")

def join_example():
    """Demonstrate a JOIN operation using SQLAlchemy."""
    print("\n--- Books with Authors ---")
    results = session.query(Book.title, Author.name.label('author'), Book.year_published)\
                    .join(Author)\
                    .order_by(Book.year_published)\
                    .all()
    
    for record in results:
        print(f"'{record.title}' by {record.author} ({record.year_published})")

def aggregation():
    """Demonstrate aggregation and GROUP BY using SQLAlchemy."""
    print("\n--- Books Count by Author ---")
    results = session.query(Author.name, func.count(Book.book_id).label('book_count'))\
                    .outerjoin(Book)\
                    .group_by(Author.author_id)\
                    .all()
    
    for record in results:
        print(f"Author: {record.name}, Books: {record.book_count}")

def advanced_query():
    """Demonstrate a more advanced query with multiple conditions using SQLAlchemy."""
    print("\n--- Books by UK authors published after 1950 ---")
    results = session.query(Book.title, Author.name, Book.year_published)\
                    .join(Author)\
                    .filter(Author.country == 'UK')\
                    .filter(Book.year_published > 1950)\
                    .order_by(Book.year_published)\
                    .all()
    
    for record in results:
        print(f"'{record.title}' by {record.name} ({record.year_published})")

if __name__ == "__main__":
    # Run all example queries
    basic_select()
    filtering()
    join_example()
    aggregation()
    advanced_query()
    
    # Close the session
    session.close() 