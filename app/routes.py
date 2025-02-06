import json

from flask import (
    flash,
    current_app,
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)


main_routes = Blueprint("main_routes", __name__)

with open("section.json") as f:
    data = json.load(f)


# Login Page
@main_routes.route("/")
def login():
    """Renders the login page."""
    if not current_app.config.get("LOGIN_REQUIRED", True):
        return redirect(url_for("main_routes.index"))

    username = session.get("username")
    if username:
        return redirect(url_for("main_routes.index"))

    return render_template("login.html")


# Home page
@main_routes.route("/index")
def index():
    # Generate URLs for each section
    sections = [
        {
            "url": url_for(f"main_routes.{section['endpoint']}"),
            "title": section["title"],
            "subtitle": section["subtitle"],
        }
        for section in data["sections"]
    ]
    return render_template("index.html", sections=sections)


# Auth API
@main_routes.route("/auth", methods=["POST"])
def auth():
    username = request.form["username"]
    password = request.form["password"]

    if current_app.config.get("PASSWORD") == password and current_app.config.get(
        "USERNAME"
    ):
        session["username"] = username
        return redirect(url_for("main_routes.index"))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for("main_routes.login"))


@main_routes.route("/index/datamine")
def datamine():
    return render_template("temp.html")


@main_routes.route("/index/model_deployment")
def model_deployment():
    return render_template("temp.html")


@main_routes.route("/index/model_training")
def model_training():
    return render_template("temp.html")
