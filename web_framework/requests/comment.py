from web_framework.api_base_model import ApiBaseModel


class CommentRequest(ApiBaseModel):
    text: str
    user_id: int

    @classmethod
    def from_json(cls, data):
        return cls(
            text=str(data['text']),
            user_id=int(data['user_id'])

        )
