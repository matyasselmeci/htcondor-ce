import re

def hello(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return ["hello\n"]

urls = [
    (re.compile(r'^hello/*$'), hello),
]
