from flask import Blueprint, render_template

views = Blueprint(__name__, "views")




@views.route("/")
def home():
	return str(render_template("header.html")+render_template("index.html")+render_template("footer.html"))

@views.route("/about")
def about():
	return str(render_template("header.html")+render_template("about.html")+render_template("footer.html"))

@views.route("/projects")
def projects():
	return str(render_template("header.html")+render_template("projects.html")+render_template("footer.html"))
