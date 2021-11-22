def application(environ, start_response):
    start_response('200 OK', [('Content-Tpye', 'text/html')])
    return [b'<h1>Hello, web</h1>']
