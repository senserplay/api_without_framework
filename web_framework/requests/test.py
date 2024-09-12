from web_framework.api_base_model import ApiBaseModel


class TestRequest(ApiBaseModel):
    param1: str
    param2: str

    @classmethod
    def from_json(cls, data):
        return cls(
            param1=str(data['param1']),
            param2=str(data['param2'])
        )