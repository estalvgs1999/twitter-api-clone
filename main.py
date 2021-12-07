# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.datastructures import UploadFile
from fastapi.params import Body, Cookie, File, Form, Header, Path, Query
from starlette import status


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
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
def home():
    return { "Hello": "World" }


# Request and Response Body
# (...) -> required param
@app.post(
    path="/person/new",
    response_model = PersonDTO,
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    summary="Create Person"
)
def create_person(person: Person = Body(...)):
    '''
    ## Create Person

    This path operation creates a person in the app and save the information in the database.

    ### Args:
    - Request body parameter:
        - **person: Person** -> A person model with first name, last name, age, hair color and marital status.

    ### Returns:
    A person model with first name, last name, age, hair color and marital status.
    '''
    return person

# Validations: Query Paramas

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
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
    """
    ## Show Person

    [summary]

    ### Args:
        name: Person name.
        age: Person Age.

    ### Returns:
        json: Person model with name and age.
    """

    return { "name": name, "age": age }


# Validations: Path Parameters

persons_db = [1,2,3,4,5]

@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Perdon Id",
        description="This is the person id. It's required and must be greater than zero",
        example=10988,
        tags=["Persons"]
    )
):
    """
    ## Show Person by Id

    [summary]

    ### Args:
        person_id : .

    ### Raises:
        HTTPException: [description]

    ### Returns:
        json: [description]
    """

    if person_id not in persons_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exists"
        ) 
    return { "person_id": person_id, "exists": True}


# Validations: Request Body

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
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
    """
    ## Update Person

    [summary]

    ### Args:
        person_id: [description].
        person: [description].

    ### Returns:
        [type]: [description]
    """
    return person

# Forms

@app.post(
    path="/login",
    response_model=LoginDTO,
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
)
def login(username: str = Form(...), password: str = Form(...)):
    """
    ## User Login

    [summary]

    ### Args:
        username (str): [description].
        password (str): [description].

    ### Returns:
        [type]: [description]
    """
    return LoginDTO(username=username)


# Cookies & Headers parameters

@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
    tags=["Contact"]
)
def contact(
    first_name: str = Form(
        ...,
        min_length=1,
        max_length=20,
        example="John"
    ),
    last_name: str = Form(
        ...,
        min_length=1,
        max_length=20,
        example="Wick"
    ),
    email: EmailStr = Form(..., example="jonhwick@gmail.com"),
    message: str = Form(
        ...,
        min_length=20,
        max_length=200,
        example="Dear developers, i want a feature that allows me to update my status. Thanks."
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    """
    ## Contact Form

    [summary]

    ### Args:
        first_name (str): [description].
        last_name (str): [description].
        email (EmailStr): [description]. 
        message (str): [description]. 
        user_agent (Optional[str], optional): [description].
        ads (Optional[str], optional): [description].

    ### Returns:
        [type]: [description]
    """
    return user_agent


# Files 

@app.post(
    path="/post-image",
    tags=["Posts"]
)
def post_image(
    image: UploadFile = File(...)
):
    """  
    ## Post Image
    
    [summary]

    ### Args:
        image (UploadFile): [description].

    ### Returns:
        [type]: [description]
    """

    return {
        "filename": image.filename,
        "format": image.content_type,
        "size": image_size(image),
    }

# Utils

def image_size(image: UploadFile) -> int:
    """
    ## Get Image Size
    
    [summary]

    ### Args:
        image (UploadFile): [description]

    ### Returns:
        int: [description]
    """
    size_bytes = len(image.file.read())
    size_kilobytes = round(size_bytes/1024, ndigits=2)
    return str(size_kilobytes)+" kB"
