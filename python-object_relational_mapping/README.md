# Python Object-Relational Mapping

This project introduces the use of Python with MySQL databases and
Object-Relational Mapping. The first tasks use MySQLdb to connect to
MySQL and execute SQL queries. Later tasks use SQLAlchemy to work with
database objects through an ORM.

## Requirements

- Python 3.8
- MySQL 8.0
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- pycodestyle 2.8.x

## Task 0

The `0-select_states.py` script connects to a MySQL server running on
localhost on port 3306 and lists all states from the specified database.
The states are displayed in ascending order by their ID.

The script accepts three arguments:

1. MySQL username
2. MySQL password
3. Database name

Example:

```bash
./0-select_states.py root root hbtn_0e_0_usa
