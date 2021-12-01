# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI,Body

app = FastAPI()

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return { "Hello": "World" }


# Request and Response Body
# (...) -> required param
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person