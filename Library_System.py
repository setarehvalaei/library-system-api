from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

books = []

class Book(BaseModel):
    id: int
    title: str
    author: str
    
class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    
@app.get("/")
def home():
    return {"message": "welcome to LIbrary System"}

@app.get("/books")
def book_list():
    return books 
    
@app.post("/books", status_code=201)
def add_book(book : Book):
    for existing_book in books:
        if existing_book.id == book.id:
            raise HTTPException(
                status_code=409,
                detail="Book already exists"
            )
            
    books.append(book)
    return book

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book_id == book.id:
            return book
    else:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
            
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book_id == book.id:
            books.remove(book)
            return "deleted!"
    else:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
        
@app.patch("/books/{book_id}")
def update_book(book_id: int, updated_book: BookUpdate):
    for book in books:
        if book.id == book_id:
            if updated_book.title is not None:
                book.title = updated_book.title

            if updated_book.author is not None:
                book.author = updated_book.author

            return book

    raise HTTPException(
            status_code=404,
            detail="Book not found"
        )