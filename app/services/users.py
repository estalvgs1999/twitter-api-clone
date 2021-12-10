import json, os
from models.user import User, UserRegister

db_dir = os.getenv("DB_PATH")

class UserService:

    def signup(self, user: UserRegister):
        """
        This method register a user in the app.

        Args:
            user (User): Request body parameter.

        Returns:
            User: Returns json with the basic user information.
        """
        with open(f"{db_dir}/users.json", "r+", encoding="utf-8") as f:
            results = json.loads(f)
            user_dict = user.dict()
            user_dict["user_id"] = str(user_dict["user_id"])
            user_dict["birth_date"] = str(user_dict["birth_date"])
            results.append(user_dict)
            f.seek(0) # Moving to first byte of the file
            json.dumps(results,f)
            return user