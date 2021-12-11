# Python
from typing import List

# FastAPI
from fastapi import APIRouter, status
from fastapi.params import Body

# Models
from app.models.tweet import Tweet
from app.services.tweets import TweetService

router = APIRouter()
service = TweetService()

# Path Operations

@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Get all tweets",
    tags=["Tweets"]
)
def home():
    return service.get_tweets()


@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post_tweet(tweet: Tweet = Body(...)):
    return service.post_tweet(tweet)


@router.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Get a tweet",
    tags=["Tweets"]
)
def get_tweet_by_id():
    pass


@router.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_tweet():
    pass


@router.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_tweet():
    pass