from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class Book:
    title: str
    author: str
    year: int


# Этот код работает, хотя год передан строкой, а автор — None
book = Book(title="Гарри Поттер", author=None, year="2000")
print(book)

class Book(BaseModel):
    title: str
    author: str
    year: int

book = Book(title="Гарри Поттер", author='', year=2000)
print(book)
