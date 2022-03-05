from app import util
from app.data.db import TweetsRepository
from app.models.tweet import Tweet

repository = TweetsRepository()

class TweetService:

    def post_tweet(self, tweet: Tweet):
        """
        This method post a new tweet in the app.

        Args:
            tweet (Tweet): Request body parameter.

        Returns:
            Tweet: Returns json with the created tweet.
        """

        results = repository.read()
        tweet_dict = util.serialize(tweet.dict())
        results.append(tweet_dict)
        repository.write(results)
        return tweet


    def get_tweets(self):
        """
        Shows all tweets in the app.

        Returns:
            List(Tweet): List with all tweets in the app.
        """
        return repository.read()