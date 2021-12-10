# Python
from typing import List

# FastAPI
from fastapi import FastAPI, status

from routers import users, tweets

app = FastAPI()

# Routes

app.include_router(users.router)
app.include_router(tweets.router)