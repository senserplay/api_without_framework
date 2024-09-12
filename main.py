from web_framework.my_web_framework import MiniWebFramework
from web_framework.endpoints import test,users

app = MiniWebFramework()
app.add_router(test.router)
app.add_router(users.router)

app.start()
