import os
from dotenv import load_dotenv
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask import Flask
from main import main
from posts import posts
from projects import projects

load_dotenv()

server = Flask(__name__)
server.config['MONGODB_HOST'] = os.getenv('DB_CONNECTION')
CORS(server)
MongoEngine(server)
server.register_blueprint(main, url_prefix="/")
server.register_blueprint(posts, url_prefix="/posts")
server.register_blueprint(projects, url_prefix="/projects")

if __name__ == '__main__':
	server.run() 




