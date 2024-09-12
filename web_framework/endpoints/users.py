import json

from web_framework.my_router import Router
from web_framework.requests.user import UserRequest
from web_framework.responses.user import UsersResponse, UserResponse
from orm.models.user import User

router = Router()


@router.get('/users')
def get_users() -> UsersResponse:
    users = User.all()
    return UsersResponse.from_orm(users)


@router.get('/user/{id}')
def get_user(id: int) -> UserResponse:
    user = User.get_by_param("id", id)

    if user is None:
        return {"error": "User not found"}, 404

    return UserResponse.from_orm(user)


@router.post('/user')
def create_user(request_body: str) -> UserResponse:
    data = json.loads(request_body)
    request = UserRequest.from_json(data)
    user = User(name=request.name, email=request.email)
    user.save()
    return UserResponse.from_orm(user)
