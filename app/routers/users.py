# Python
from typing import List

# FastAPI
from fastapi import APIRouter, status
from fastapi.params import Body
from app.services.users import UserService

# Models
from app.models.user import User, UserRegister

router = APIRouter()
service = UserService()

# Path Operations
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    This path operation register a user in the app.

    **Args:**
        user (UserRegister, optional): New user.

    **Returns:**
        User: Returns a json with the basic user information.
    """
    return service.signup(user)


@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
)
def login():
    pass


@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    tags=["Users"]
)
def get_all_users():
    """
    Shows all users in the app.

    **Returns:**
        List[User]: List with all users in the app.
    """
    return service.get_all()


@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get user by id",
    tags=["Users"]
)
def get_user_by_id():
    pass


@router.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
)
def update_user():
    pass


@router.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_user():
    pass
