import json

#from web_framework.my_router import Router
from fastapi import APIRouter
from web_framework.requests.comment import CommentRequest
from web_framework.responses.comment import CommentResponse, CommentsResponse
from orm.models.comment import Comment

router = APIRouter()


@router.get('/comments/{article_id}')
def get_comments(article_id: int):
    comments = Comment.get_by_param("article_id", article_id)
    return CommentsResponse.from_orm(comments)


@router.post('/comment/{article_id}')
def create_comment(article_id: int, request: CommentRequest) -> CommentResponse:
    # data = json.loads(request_body)
    # request = CommentRequest.from_json(data)
    comment = Comment(text=request.text, user_id=request.user_id, article_id=article_id)
    comment.save()
    return CommentResponse.from_orm(comment)

