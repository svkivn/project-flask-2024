from app import app
from wsgiref.simple_server import make_server


server = make_server('localhost', 8000, app)
server.serve_forever()