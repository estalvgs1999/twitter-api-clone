from app.data.db import UsersRepository
from app.models.user import UserRegister

repository = UsersRepository()

class UserService:

    def signup(self, user: UserRegister):
        """
        This method register a user in the app.

        Args:
            user (User): Request body parameter.

        Returns:
            User: Returns json with the basic user information.
        """

        results = repository.read()
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        repository.write(results)
        return user


    def get_all(self):
        """
        Shows all users in the app.

        Returns:
            List(User): List with all users in the app.
        """
        return repository.read()
