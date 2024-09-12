import socket
import re


class MiniWebFramework:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.routes = {
            'GET': {},
            'POST': {},
            'PUT': {},
            'DELETE': {}
        }

    def add_router(self, router, prefix=""):
        for method, routes in router.routes.items():
            for path, handler in routes.items():
                full_path = f"{prefix}{path}"
                self.routes[method][full_path] = handler

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"Serving on {self.host}:{self.port}")

        while True:
            client_socket, addr = server_socket.accept()
            request_data = client_socket.recv(1024).decode('utf-8')
            headers, body = self.parse_request(request_data)

            method, request_path, _ = headers['Request-Line'].split(' ', 2)

            handler, params = self.find_handler(method, request_path)

            if handler:
                # Если это POST-запрос, передаем тело запроса в обработчик
                if method == "POST":
                    response = handler(body, **params)
                else:
                    response = handler(**params)

                response_body = f"HTTP/1.1 200 OK\n\n{response}"
            else:
                response_body = "HTTP/1.1 404 Not Found\n\n404 Not Found"

            client_socket.sendall(response_body.encode('utf-8'))
            client_socket.close()

    def parse_request(self, request_data):
        """ Парсим заголовки и тело запроса """
        parts = request_data.split('\r\n\r\n', 1)
        headers_part = parts[0]
        body = parts[1] if len(parts) > 1 else ''

        headers = {}
        lines = headers_part.split('\r\n')
        headers['Request-Line'] = lines[0]
        for line in lines[1:]:
            key, value = line.split(': ', 1)
            headers[key] = value

        return headers, body

    def find_handler(self, method, request_path):
        for path_regex, handler in self.routes.get(method, {}).items():
            match = re.match(path_regex, request_path)
            if match:
                return handler, match.groupdict()
        return None, {}

