from web_framework.my_web_framework import MiniWebFramework
from web_framework.endpoints import article, user, comment
from fastapi import FastAPI

#app = MiniWebFramework()

app_kwargs = {
    "title": "API",
    "description": "API",
    "version": "1.0.0",
}

app = FastAPI(**app_kwargs)
app.include_router(article.router)
app.include_router(user.router)
app.include_router(comment.router)

#app.start()
