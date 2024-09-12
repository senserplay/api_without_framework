import json

from web_framework.my_router import Router
from web_framework.requests.test import TestRequest
from web_framework.responses.test import TestResponse

router = Router()


@router.get('/test/{id}')
def get_test(id: int):
    return {'id': id, 'type': type(id)}


@router.post('/test')
def post_test(request_body: str) -> TestResponse:
    data = json.loads(request_body)
    request = TestRequest.from_json(data)
    print(request)
    return TestResponse(param1=request.param1,param2=request.param2)
