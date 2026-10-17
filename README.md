# Library System API

A simple library management system built with **Python** and **FastAPI**.

This project was created as a learning project to practice building REST APIs. It allows users to add, view, update, and delete books.

## Features

- Get a list of all books
- Add a new book
- Get a specific book by ID
- Update book information using PATCH
- Delete a book by ID
- Prevent duplicate book IDs
- Handle errors for books that do not exist

## Technologies Used

- Python
- FastAPI
- Pydantic

## Data Storage

This project does not use a database. Book information is stored in a Python list in memory.

**Note:** Book data is lost when the application stops or restarts.

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment if needed.
4. Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the development server:

```bash
python -m fastapi dev Library_System.py
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Get all books |
| POST | `/books` | Add a new book |
| GET | `/books/{book_id}` | Get a book by ID |
| PATCH | `/books/{book_id}` | Update a book |
| DELETE | `/books/{book_id}` | Delete a book |

## API Documentation

After starting the server, open the interactive API documentation:

http://127.0.0.1:8000/docs

## Purpose

The purpose of this project is to practice Python, FastAPI, HTTP methods, request validation, and basic error handling.