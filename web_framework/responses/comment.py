from orm.models.comment import Comment
from web_framework.api_base_model import ApiBaseModel
from typing import List


class CommentResponse(ApiBaseModel):
    id: int
    text: str
    article_id: int
    user_id: int

    @classmethod
    def from_orm(cls, comment: Comment):
        return cls(
            id=comment.id,
            text=comment.text,
            article_id=comment.article_id,
            user_id=comment.user_id
        )


class CommentsResponse(ApiBaseModel):
    comments: List[CommentResponse]

    @classmethod
    def from_orm(cls, comments: List[Comment]):
        return cls(
            comments=[CommentResponse.from_orm(comment) for comment in comments]
        )
