from wsgiref import simple_server as ss


def server():
    server = ss.make_server("0.0.0.0", 9898, ss.demo_app)
    print "Webbrower url port :9898 ......."
    server.serve_forever()

server()
