from orm.models.article import Article
from web_framework.api_base_model import ApiBaseModel
from typing import List


class ArticleResponse(ApiBaseModel):
    id: int
    title: str
    text: str
    user_id: int

    @classmethod
    def from_orm(cls, article: Article):
        return cls(
            id=article.id,
            title=article.title,
            text=article.text,
            user_id=article.user_id
        )


class ArticlesResponse(ApiBaseModel):
    articles: List[ArticleResponse]

    @classmethod
    def from_orm(cls, articles: List[Article]):
        return cls(
            articles=[ArticleResponse.from_orm(article) for article in articles]
        )
