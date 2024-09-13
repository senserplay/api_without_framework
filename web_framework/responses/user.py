from orm.models.user import User
from web_framework.api_base_model import ApiBaseModel
from typing import List


class UserResponse(ApiBaseModel):
    id: int
    name: str
    email: str
    login: str
    password: str

    @classmethod
    def from_orm(cls, user: User):
        return cls(
            id=user.id,
            name=user.name,
            email=user.email,
            login=user.login,
            password=user.password
        )


class UsersResponse(ApiBaseModel):
    users: List[UserResponse]

    @classmethod
    def from_orm(cls, users: List[User]):
        return cls(
            users = [UserResponse.from_orm(user) for user in users]
        )
