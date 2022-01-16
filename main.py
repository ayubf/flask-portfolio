from flask import Blueprint, render_template

from models.Posts import Posts
from models.Projects import Projects

main = Blueprint(__name__, "main")


@main.route("/", methods=['GET'])
def home():
	postData = Posts.objects.order_by('-id')[:4]
	projectData = Projects.objects.order_by('-id')[:4]

	return render_template("index.j2", data={
		"postData": postData,
		"projectData": projectData
	})

@main.route("/about", methods=['GET'])
def about():
	return render_template("about.j2")



