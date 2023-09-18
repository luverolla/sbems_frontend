"""
This is a sample Python Flask application that demonstrates how to connect to
"""

import os
import sys
from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory

base_dir = "."
if hasattr(sys, "_MEIPASS"):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(
    __name__,
    static_folder=os.path.join(base_dir, "static"),
    template_folder=os.path.join(base_dir, "templates"),
)


@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""
    return "<p>Hello, World!</p>"


@app.route("/users/<name>/")
def userpage(name: str):
    """Return a custom greeting to the user"""
    return render_template("userpage.j2", name=name)


@app.route("/users/")
def userlist():
    """Return a list of users"""
    return render_template("userlist.j2", users=["Alice\n\n", "\t\tBob", "Carol"])


@app.route("/files")
def filelist():
    """Return a list of files"""
    print(os.listdir(os.path.join(base_dir, "uploads")))
    filesdir = os.path.join(base_dir, "uploads")
    file_list = os.listdir(filesdir)
    return render_template("filelist.html", files=file_list)


@app.route("/files/<filename>")
def file(filename: str):
    """Return the contents of a file"""
    filesdir = os.path.abspath(os.path.join(base_dir, "uploads"))
    return send_from_directory(filesdir, filename, as_attachment=True)


def main(debug=False):
    """Run the app"""
    load_dotenv()
    host = os.getenv("SRV_ADDR")
    port = os.getenv("SRV_PORT")
    app.run(host, port, debug)


if __name__ == "__main__":
    main(debug=True)
