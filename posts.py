
from flask import Blueprint, render_template, request
import datetime
from models.Posts import Posts
import os
from dotenv import load_dotenv

load_dotenv()


posts = Blueprint(__name__, "posts")

@posts.route('/', methods=['GET'])
def getPosts():
    data = Posts.objects.order_by('-id')
    return render_template("posts.j2",data=data)


@posts.route('/<string:title>', methods=['GET'])
def getOnePost(title):
    try:
        post = Posts.objects.get(titleURL=title)
        post.update(views=post.views+1)
        data = {
            "title": post.title,
            "body": post.body,
            "date": post.date
        }
        return render_template("post.j2", data=data)
    except:
        return render_template("notfound.j2")




@posts.route('/create', methods=['POST'])
def createPost():
    if request.json['key'] == os.getenv('KEY'):
        newPost = Posts(title=request.json['title'], titleURL=request.json['title'].lower().replace(' ','-'), body=request.json['body'])
        newPost.save()
        return {"message": "Post sucessfully created"}, 200
    else:
        return {"message": "Post creation unsuccessful"}, 403
