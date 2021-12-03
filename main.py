# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query, Path, Form

app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class PersonBase(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1, 
        max_length=50,
        example="John"
    )
    last_name: str = Field(
        ..., 
        min_length=1, 
        max_length=50,
        example="Wick"
    )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=34
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None, example=False)


class Person(PersonBase):
    
    password: str = Field(
        ...,
        min_length=8,
        example="seCure_Pa55w0r6"
    )


    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "John",
    #             "last_name": "Wick",
    #             "age": 34,
    #             "hair_color": "black",
    #             "is_married": False
    #         }
    #     }


class PersonDTO(PersonBase):
    pass


class LoginDTO(BaseModel):
    username: str = Field(
        ...,
        max_length=20,
        example="my_user"
    )
    message: str = Field(default="Login successful")


class Location(BaseModel):
    city: str
    state: str
    country: str


@app.get(
    path="/",
    status_code=status.HTTP_200_OK
)
def home():
    return { "Hello": "World" }


# Request and Response Body
# (...) -> required param
@app.post(
    path="/person/new",
    response_model = PersonDTO,
    status_code=status.HTTP_201_CREATED
)
def create_person(person: Person = Body(...)):
    return person

# Validations: Query Paramas

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK
)
def show_person(
    name: Optional[str] = Query(
        default=None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters",
        example="John"
        ),
    age: int = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required",
        example=34
    )
):
    return { "name": name, "age": age }


# Validations: Path Parameters

@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Perdon Id",
        description="This is the person id. It's required and must be greater than zero",
        example=10988
    )
):
    return { "person_id": person_id, "exists": True}


# Validations: Request Body

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_200_OK
)
def update_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person Id",
        description="This is the person id. It's required and must be greater than zero",
        example=10988
    ),
    person: Person = Body(...)
):
    return person


@app.post(
    path="/login",
    response_model=LoginDTO,
    status_code=status.HTTP_200_OK
)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginDTO(username=username)