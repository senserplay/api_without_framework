from web_framework.api_base_model import ApiBaseModel


class UserRequest(ApiBaseModel):
    name: str
    email: str

    @classmethod
    def from_json(cls, data):
        return cls(
            name=str(data['name']),
            email=str(data['email'])
        )