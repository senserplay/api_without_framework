import json

# from web_framework.my_router import Router
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
def get_article(id: int):
    articles = Article.get_by_param("id", id)
    if not articles:
        return {"error": "Article not found"}, 404
    return ArticleResponse.from_orm(articles[0])


@router.delete('/article/{id}')
def delete_article(id: int):
    articles = Article.get_by_param("id", id)
    if not articles:
        return {"error": "Article not found"}, 404
    articles[0].delete()
    return {"status": "ok"}


@router.post('/article')
def create_article(request: ArticleRequest) -> ArticleResponse:
    # data = json.loads(request_body)
    # request = ArticleRequest.from_json(data)
    article = Article(title=request.title, text=request.text, user_id=request.user_id)
    article.save()
    return ArticleResponse.from_orm(article)


@router.get('/user/{user_id}/article')
def get_user_articles(user_id: int):
    articles = Article.get_by_param("user_id", user_id)
    return ArticlesResponse.from_orm(articles)
