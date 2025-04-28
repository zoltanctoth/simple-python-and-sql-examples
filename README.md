# Python SQL Workshop

A simple demonstration project for teaching Python and SQL basics.

## Setup

1. Create a virtual environment and install dependencies:
   ```
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Create the database:
   ```
   python setup_db.py
   ```

3. Run the example queries:
   ```
   python query_examples.py
   ```

## Files

- `setup_db.py` - Creates a SQLite database with sample data for a bookstore
- `query_examples.py` - Contains examples of various SQL queries
- `bookstore.db` - The SQLite database file (created by running setup_db.py)

## Database Schema

### authors
- `author_id` (INTEGER, PRIMARY KEY)
- `name` (TEXT)
- `country` (TEXT)

### books
- `book_id` (INTEGER, PRIMARY KEY)
- `title` (TEXT)
- `author_id` (INTEGER, FOREIGN KEY to authors)
- `year_published` (INTEGER)
- `price` (REAL)

## Example Queries

The query_examples.py file demonstrates:
- Basic SELECT queries
- Filtering with WHERE clauses
- JOIN operations
- Aggregation with GROUP BY
- More complex queries with multiple conditions # simple-python-and-sql-examples
