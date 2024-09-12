import re
import socket

class Router:
    def __init__(self):
        self.routes = {
            'GET': {},
            'POST': {},
            'PUT': {},
            'DELETE': {}
        }

    def add_route(self, method, path, handler):
        path_regex = re.sub(r'{(\w+)}', r'(?P<\1>[^/]+)', path)
        self.routes[method][path_regex] = handler

    def get(self, path):
        def wrapper(func):
            self.add_route('GET', path, func)
            return func
        return wrapper

    def post(self, path):
        def wrapper(func):
            self.add_route('POST', path, func)
            return func
        return wrapper

    def put(self, path):
        def wrapper(func):
            self.add_route('PUT', path, func)
            return func
        return wrapper

    def delete(self, path):
        def wrapper(func):
            self.add_route('DELETE', path, func)
            return func
        return wrapper

    def get_route(self, method, path):
        for path_regex, handler in self.routes.get(method, {}).items():
            match = re.match(path_regex, path)
            if match:
                return handler, match.groupdict()
        return None, {}
