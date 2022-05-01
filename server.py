from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from json import dumps, loads
from os import getenv
from random import randint


class HTTPRequestHandler(BaseHTTPRequestHandler):
    server_id = randint(1, 100)

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _send_response(self, body=None):
        self._set_headers()

        if body is not None:
            self.wfile.write(dumps(body).encode())

    def do_HEAD(self):
        self._send_response()

    def do_GET(self):
        response = {'message': f'Welcome to server { self.server_id }.'}
        self._send_response(response)

    def do_POST(self):
        content_size = int(self.headers['Content-Length'])
        content_body = loads(self.rfile.read(content_size))

        # echo the content body back to the client
        self._send_response(content_body)


def main():
    addr, port = '', int(getenv('PORT', 8080))

    print(f'Server listening on {addr}:{port}')

    httpd = ThreadingHTTPServer((addr, port), HTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
