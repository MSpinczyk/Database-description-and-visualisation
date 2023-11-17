# Library revision/ideas
## SQLAlchemy:

- **Description:** SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of high-level API for communicating with relational databases, allowing you to interact with databases using Python objects instead of raw SQL queries.

- **Use in Solution:** `sqlalchemy` is used to connect to the existing database, inspect its structure, and generate SQLAlchemy model code representing the database schema.

## sqlacodegen:

- **Description:** `sqlacodegen` is a tool that generates SQLAlchemy model code from an existing database. It examines the structure of a database and produces Python code that represents the tables and relationships.

- **Use in Solution:** `sqlacodegen` is employed to automatically generate SQLAlchemy models from an existing database, making it easier to work with the database structure in Python.

## Graphviz + Kroki.io:

- **Description:** Graphviz is an open-source graph visualization software. It provides tools for creating and rendering graphs and diagrams. Graphviz supports various graph layout algorithms and produces output in multiple formats.

- **Use in Solution:** Graphviz is used to create a graphical representation of the database schema in the form of an Entity-Relationship Diagram (ERD). The `erd` tool, which is built on Graphviz, is used to generate the ERD.

## ERAAlchemy:
# NO longer supported -> eralchemy2

- **Description:** `erd` is an open-source tool that uses Graphviz to generate Entity-Relationship Diagrams (ERDs) from SQLAlchemy model code. It takes a Python file containing SQLAlchemy model definitions and produces a visual representation of the relationships between tables.

- **Use in Solution:** `erd` is utilized to automatically generate an ERD from the SQLAlchemy models created by `sqlacodegen`. The resulting diagram provides a visual overview of the database schema.


## OpenAI API
- **Use in Solution:** Textual descriptions of the database + general markdown structure