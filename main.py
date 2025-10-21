from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory book data
books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 4, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 5, "title": "Moby Dick", "author": "Herman Melville", "year": 1851},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books")
def create_book(book: dict):
    book["id"] = len(books) + 1
    books.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):
    for index, b in enumerate(books):
        if b["id"] == book_id:
            books[index].update(updated_book)
            return books[index]
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, b in enumerate(books):
        if b["id"] == book_id:
            deleted = books.pop(index)
            return {"message": "Book deleted", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")
