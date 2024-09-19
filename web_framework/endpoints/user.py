import json

# from web_framework.my_router import Router
from fastapi import APIRouter
from web_framework.requests.user import UserRequest, LoginRequest
from web_framework.responses.user import UsersResponse, UserResponse
from orm.models.user import User

router = APIRouter()


@router.get('/users')
def get_users() -> UsersResponse:
    users = User.all()
    return UsersResponse.from_orm(users)


@router.get('/user/{id}')
def get_user(id: int) -> UserResponse:
    users = User.get_by_param("id", id)

    if not users:
        return {"error": "User not found"}, 404

    return UserResponse.from_orm(users[0])


@router.post('/user')
def create_user(request: UserRequest) -> UserResponse:
    # data = json.loads(request_body)
    # request = UserRequest.from_json(data)
    user = User(name=request.name, email=request.email, login=request.login, password=request.password)
    user.save()
    return UserResponse.from_orm(user)


@router.post('/login')
def login_user(request: LoginRequest) -> UserResponse:
    login = request.login
    password = request.password

    users = User.get_by_params(login=login, password=password)

    if not users:
        return {"error": "Invalid login or password"}, 401

    return UserResponse.from_orm(users[0])
