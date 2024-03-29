## Project Overview

This project provides a solution for creating comprehensive documentation for an existing, working database. The generated documentation includes both a graphical representation of the database and a text description of its tables. The text description aims to infer semantics using table and column names, considering additional information such as comments, constraints, and relationships.

The solution leverages third-party tools for visualization and an AI chatbot API for generating textual descriptions. Specifically, it utilizes DBML (Database Markup Language) for database visualization. The result of running the program on an existing database is a PDF file containing the database description and embedded graphics with diagrams.

## Features

- Extracts database information, including table structures, indexes, and schemas.
- Utilizes [OpenAI](https://www.openai.com/) to generate natural language descriptions for each table.
- Visualizes the database schema using DBML and embeds it in the documentation.
- Converts the documentation to a PDF file for easier sharing and distribution.

## Technologies 

- **Python 3**
- **Docker**
- **PostgreSQL** is a powerful open-source relational database management system (RDBMS). It is known for its extensibility and supports a wide range of data types. In this context, it's used for connecting to databases and obtaining dump files.
- **Node.js** and **npm**: Node.js is a JavaScript runtime that allows developers to run JavaScript on the server side. npm (Node Package Manager) is the package manager for Node.js, facilitating the installation and management of JavaScript. Those packages allow us to use DBML CLI.
- **[DBML CLI](https://www.dbml.org/cli)** a package, which converts between different formats from the command line (DBML file to SQL or SQL file to DBML)
- **sqlacodegen** is a Python tool that generates SQLAlchemy code from an existing database. It automates the process of creating SQLAlchemy models based on the structure of the database.
- **[Pandoc](https://pandoc.org/)** and **[pandoc-filters](https://github.com/mittelmark/pandoc-filters)**: Pandoc is a document converter that supports various markup formats. Pandoc-filters are additional tools that can be used to extend Pandoc's functionality. They are utilized here for converting Markdown documents to PDF format.


## Installation and Usage

### Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose

### Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Build the Docker image:

    ```bash
    docker build -t database-documentation-generator .

3. Run the Docker container:

    ```bash
    docker run -v "$(pwd)":/output database-documentation-generator python3 /app/generation.py <user> <password> <host> <port> <database> <openai-key> 

Replace `<user>`, `<password>`, `<host>`, `<port>`, `<database>`, and `<openai-key>` with your actual database credentials and OpenAI API key.


4. The generated PDF will be saved in the current directory as `output.pdf`.

## Project Structure
- `generation.py`: Python script for extracting database information, generating documentation, and converting it to PDF.
- `Dockerfile`: Docker configuration for building the project as a Docker image.
- `requirements.txt`: Python dependencies for the project.
- `filter-kroki.lua`: embed diagram code and embed image links using the https://krokio.io webservice.

## Documentation
The documentation includes the following sections:

- Database name and schemas
- Indexes
- Tables with descriptions and generated natural language descriptions using OpenAI
- Visual representation of the database schema in DBML format

### Example documentation

The example documentation could be find in the repository. It is saved as `output.pdf`.

## Contributions
This project was developed by Jan Mrożek and Michał Spinczyk. Each team member contributed to different aspects of the project:
| Team Member         | Contributions                                                      |
|---------------------|-------------------------------------------------------------------|
| Jan Mrożek          | - Getting SQL syntax from database                                  |
|                     | - Getting DBML model from SQL                                      |
| Michał Spinczyk      | - Generating database description                                  |
|                     | - Generating PDF document with Pandoc                               |
| Both                | - Creating Dockerfile                                              |
|                     | - Writing README.md                                                |