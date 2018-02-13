from wsgiref import simple_server as ss


def server():
    server = ss.make_server("0.0.0.0", 9898, ss.demo_app)
    server.serve_forever()

server()
