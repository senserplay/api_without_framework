from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3003",
        "http://localhost:3002",
        "http://localhost:3001",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(article.router)
app.include_router(user.router)
app.include_router(comment.router)

#app.start()
