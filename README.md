# SQLAlchemy and SQLite Example

This repository demonstrates how to use SQLAlchemy ORM to define models and interact with an SQLite database in Python. It includes basic operations like insertion, querying, and updating records using both SQLAlchemy and the built-in `sqlite3` module.

## 🧱 Overview

The project includes:

- A SQLAlchemy model (`myfields.py`) mapped to a table called `My_Table`
- Functions for inserting, querying, updating, and deleting records (`sqlquery.py`)
- Sample scripts (`dbload.py`, `dbload2.py`, `dbload3.py`) for loading data
- A sample CSV file (`mydata.csv`) and SQLite database files (`mydatabase.db`, `sqlalchemy.db`)
- A Jupyter notebook (`test.ipynb`) for interactive exploration

## 🚀 Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jharemza/SQLAlchemy_and_sqlite.git
   cd SQLAlchemy_and_sqlite
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install sqlalchemy
   ```

## ⚙️ Usage

You can interact with the database in two ways:

### With SQLAlchemy ORM

```python
from myfields import myfields
new_rec = myfields(12.5, "example text", "2024-01-01")
```

### With sqlite3 API

```python
from sqlquery import insert_record, get_all
insert_record(new_rec)
print(get_all())
```

See `sqlquery.py` for full CRUD operations.

## 📂 File Structure

- `myfields.py`: SQLAlchemy ORM model
- `sqlquery.py`: SQLite-based record manipulation functions
- `base.py`: Declarative base
- `dbload*.py`: Data loading scripts
- `mydatabase.db`, sqlalchemy.db: SQLite DB files
- `test.ipynb`: Jupyter notebook for testing
- `mydata.csv`: Example CSV data

## 📝 License

This project is licensed under the terms of the [MIT License](LICENSE).
