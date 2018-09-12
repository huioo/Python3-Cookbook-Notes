from functools import partial
from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def __init__(self, request, client_address, server, ack):
        self.ack = ack
        super().__init__(request, client_address, server)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)


if __name__ == '__main__':
    server = TCPServer(('', 15000), partial(EchoHandler, ack='RECEIVED:'))
    server.serve_forever()
