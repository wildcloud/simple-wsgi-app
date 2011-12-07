from cherrypy import wsgiserver

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello World\n'

server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 4000), application, server_name='simple.python.application')
server.start()
