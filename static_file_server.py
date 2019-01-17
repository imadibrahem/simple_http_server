#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib import parse

HOST_NAME = 'localhost'
PORT_NUMBER = 8080
ROOTDIR = './www/' 

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith('.html'):
                with open(ROOTDIR + self.path, "rb") as f:

                    self.send_response(200)

                    self.send_header('Content-type','text-html')
                    self.end_headers()

                    self.wfile.write(f.read())
            else:
                self.send_error(404, 'file not found')

        except IOError:
            self.send_error(404, 'file not found')


if __name__ == '__main__':
    server = HTTPServer((HOST_NAME, PORT_NUMBER), GetHandler)
    print('Starting server')
    server.serve_forever()
