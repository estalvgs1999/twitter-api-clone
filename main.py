# Python
from typing import Optional
from fastapi.datastructures import Default
# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Body, Query

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

# Validations for Query Paramas

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50
    ),
    age: str = Query(...)
):
    return {
        "name": name,
        "age": age 
    }