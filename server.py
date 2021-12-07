from flask import Flask
from views import views

server = Flask(__name__) # Flask object
server.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
	server.run() # By default port 5k but port= option can change that




