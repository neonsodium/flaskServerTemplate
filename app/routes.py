import json

from flask import (
    Flask,
    abort,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    send_file,
    send_from_directory,
    session,
    url_for,
)
from werkzeug.utils import secure_filename

from app import app

with open("section.json") as f:
    data = json.load(f)


# Login Page
@app.route("/")
def login():
    """Renders the login page."""
    if not app.config.get("LOGIN_REQUIRED", True):
        return redirect(url_for("index"))

    username = session.get("username")
    if username:
        return redirect(url_for("index"))

    return render_template("login.html")


# Home page
@app.route("/index")
def index():
    # Generate URLs for each section
    sections = [
        {
            "url": url_for(section["endpoint"]),
            "title": section["title"],
            "subtitle": section["subtitle"],
        }
        for section in data["sections"]
    ]
    return render_template("index.html", sections=sections)


# Auth API
@app.route("/auth", methods=["POST"])
def auth():
    username = request.form["username"]
    password = request.form["password"]

    if app.config.get("PASSWORD") == password and app.config.get("USERNAME"):
        session["username"] = username
        return redirect(url_for("index"))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for("login"))


@app.route("/index/datamine")
def datamine():
    return render_template("temp.html")


@app.route("/index/model_deployment")
def model_deployment():
    return render_template("temp.html")


@app.route("/index/model_training")
def model_training():
    return render_template("temp.html")
