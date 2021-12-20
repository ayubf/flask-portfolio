from flask import Blueprint, render_template

views = Blueprint(__name__, "views")




@views.route("/")
def home():
	return render_template("index.j2")

@views.route("/about")
def about():
	return render_template("about.j2")

@views.route("/projects")
def projects():
	return render_template("projects.j2")
