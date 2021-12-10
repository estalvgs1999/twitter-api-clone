import json, os
from typing import List

class Repository:

    def read(self) -> List:
        with open(self.file_path, "r+", encoding="utf-8") as f:
            users = json.loads(f.read())
            return users

    def write(self, users: List):
        with open(self.file_path, "r+", encoding="utf-8") as f:
            f.seek(0) # Moving to first byte of the file
            f.write(json.dumps(users))


class UsersRepository(Repository):

    def __init__(self) -> None:
        super().__init__()
        self.file_path = os.getenv("USERS_DB")
        


class TweetsRepository(Repository):

    def __init__(self) -> None:
        super().__init__()
        self.file_path = os.getenv("TWEETS_DB")