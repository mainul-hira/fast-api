from enum import Enum

from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'first book', 'author': 'first author'},
    'book_2': {'title': 'second book', 'author': 'second author'},
    'book_3': {'title': 'third book', 'author': 'third author'}
}


class DirectionName(str, Enum):
    North = "North"
    South = "South"
    West = "West"
    East = "East"


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/books/mybook")
async def read_favourite_book():
    return {"book_title": "Favourite book"}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_title": book_id}


@app.get('/directions/{direction_name}')
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.North:
        return {"direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.South:
        return {"direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.West:
        return {"direction": direction_name, "sub": "Left"}
    return {"direction": direction_name, "sub": "Right"}
