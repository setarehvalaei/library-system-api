# Library System API

A simple Library System API built with Python and FastAPI. This project allows users to manage books through HTTP requests.

## Features

- **Get all books:** Retrieve all books stored in the system.
- **Add a book:** Add a new book with an ID, title, and author.
- **Get a book:** Retrieve a specific book using its ID.
- **Update a book:** Update the title or author of an existing book.
- **Delete a book:** Remove a book from the system.
- **Duplicate ID validation:** Prevent adding books with an existing ID.
- **Error handling:** Return appropriate error messages when a book is not found.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Data Storage

Books are stored in a Python dictionary in memory. Each book's ID is used as the dictionary key, and its title and author are stored as the value.

**Note:** This project does not use a database. All book data is lost when the application stops or restarts.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/setarehvalaei/library-system-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd library-system-api
   ```

3. Create and activate a virtual environment (optional but recommended).

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Run the following command:

```bash
uvicorn Library_System:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation. After starting the application, open:

`http://127.0.0.1:8000/docs`

You can use this page to test all endpoints.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/books` | Get all books |
| POST | `/books` | Add a new book |
| GET | `/books/{book_id}` | Get a book by ID |
| PATCH | `/books/{book_id}` | Update a book |
| DELETE | `/books/{book_id}` | Delete a book |

## Example Request

To add a book, send a `POST` request to `/books` with the following JSON body:

```json
{
  "id": 1,
  "title": "Python Basics",
  "author": "Ali"
}
```

## Learning Goals

This project was created to practice building REST APIs with FastAPI, using Pydantic models, handling HTTP errors, and managing data with Python dictionaries.