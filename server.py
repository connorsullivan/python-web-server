import os
import random

from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


class MyHandler(SimpleHTTPRequestHandler):
    server_id = random.randint(1, 100)

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()

        msg = f'Your magic number is { self.server_id }.'

        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))

httpd = TCPServer(('', port), MyHandler)
httpd.serve_forever()
