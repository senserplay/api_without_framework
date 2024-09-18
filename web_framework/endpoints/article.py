import json

#from web_framework.my_router import Router
from fastapi import APIRouter
from web_framework.requests.article import ArticleRequest
from web_framework.responses.article import ArticleResponse, ArticlesResponse
from orm.models.article import Article

router = APIRouter()


@router.get('/articles')
def get_articles() -> ArticlesResponse:
    articles = Article.all()
    return ArticlesResponse.from_orm(articles)


@router.get('/article/{id}')
def get_article(id: int) -> ArticleResponse:
    article = Article.get_by_param("id", id)

    if article is None:
        return {"error": "Article not found"}, 404
    return ArticleResponse.from_orm(article[0])


@router.post('/article')
def create_article(request: ArticleRequest) -> ArticleResponse:
    # data = json.loads(request_body)
    # request = ArticleRequest.from_json(data)
    article = Article(title=request.title, text=request.text, user_id=request.user_id)
    article.save()
    return ArticleResponse.from_orm(article)
