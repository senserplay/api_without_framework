from web_framework.api_base_model import ApiBaseModel


class ArticleRequest(ApiBaseModel):
    title: str
    text: str
    user_id: int

    @classmethod
    def from_json(cls, data):
        return cls(
            title=str(data['title']),
            text=str(data['text']),
            user_id=int(data['user_id'])

        )
