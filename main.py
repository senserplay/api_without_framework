from web_framework.my_web_framework import MiniWebFramework
from web_framework.endpoints import article, user

app = MiniWebFramework()
app.add_router(article.router)
app.add_router(user.router)

app.start()
