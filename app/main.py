# FastAPI
from fastapi import FastAPI

from app.routers import users, tweets

app = FastAPI()

# Routes

app.include_router(users.router)
app.include_router(tweets.router)