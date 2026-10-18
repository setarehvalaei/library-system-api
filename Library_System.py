from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

books = {}

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
def book_dict():
    return books
    
@app.post("/books", status_code=201)
def add_book(book: Book):
    if book.id in books:
        raise HTTPException(
            status_code=409,
            detail="Book already exists"
        )

    books[book.id] = {
        "title": book.title,
        "author": book.author
    }

    return books[book.id]


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id in books:
        return books[book_id]

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
            
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id in books:
        books.pop(book_id)
        return "deleted!"
        
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
        
@app.patch("/books/{book_id}")
def update_book(book_id: int, updated_book: BookUpdate):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    if updated_book.title is not None:
        books[book_id]["title"] = updated_book.title

    if updated_book.author is not None:
        books[book_id]["author"] = updated_book.author

    return books[book_id]