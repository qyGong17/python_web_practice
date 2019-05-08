# hello.py


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # PATH_INFO example: 'http://localhost:8888/gqy', then environ['PATH_INFO'][1:]='gqy'
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
