"""
controllers/main_controller.py
Controller layer — a Blueprint that wires URL routes to model data
and view templates. Keeps request handling separate from both the
data (models/project.py) and presentation (templates/).
"""

from flask import Blueprint, render_template, abort
from models.project import get_all_projects, get_project

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    projects = get_all_projects()
    return render_template("index.html", projects=projects)


@main_bp.route("/projects/<slug>/")
def project_detail(slug):
    project = get_project(slug)
    if project is None:
        abort(404)
    return render_template("project_detail.html", project=project)


@main_bp.route("/about/")
def about():
    return render_template("about.html")


@main_bp.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404
