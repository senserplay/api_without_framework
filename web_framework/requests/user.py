from web_framework.api_base_model import ApiBaseModel


class UserRequest(ApiBaseModel):
    name: str
    email: str
    login: str
    password: str

    @classmethod
    def from_json(cls, data):
        return cls(
            name=str(data['name']),
            email=str(data['email']),
            login=str(data['login']),
            password=str(data['password'])
        )


class LoginRequest(ApiBaseModel):
    login: str
    password: str
