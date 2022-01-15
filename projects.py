from flask import Blueprint, render_template, request
import datetime
from models.Projects import Projects
import os
from dotenv import load_dotenv

load_dotenv()

projects = Blueprint(__name__, "projects")

@projects.route('/create', methods=['POST'])
def createProj():
    if request.json['key'] == os.getenv('KEY'):
        newProj = Projects(title=request.json['title'], titleURL=request.json['title'].lower().replace(' ','-'), miniText=request.json['miniText'], technologies=request.json['technologies'])
        newProj.save()
        return {"message": "Project sucessfully created"}, 200
    else:
        return {"message": "Project creation unsuccessful"}, 403

@projects.route('/', methods= ['GET'])
def getProjects():
    data = Projects.objects.order_by('-id')
    return render_template("projects.j2", data=data)

@projects.route('/<string:title>', methods=['GET'])
def getOneProject(title):
    try:
        project = Projects.objects.get(titleURL=title)
        data = {
            "title": project.title,
            "titleURL": project.titleURL,
            "miniText": project.miniText,
            "technologies": project.technologies,
        }
        return render_template("project.j2", data=data)
    except:
        return render_template("notfound.j2")

    