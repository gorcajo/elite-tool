import json
import logging

from flask import Flask
from flask import redirect
from flask import request
from flask import send_from_directory
from werkzeug.exceptions import NotFound


app = Flask(__name__)

logging.basicConfig(
    format="%(levelname).4s | %(asctime)s.%(msecs)03d | %(threadName)-12s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO)


@app.route("/", methods=["GET"])
def get_root():
    return redirect("/home", code=302)


@app.route("/<section>", methods=["GET"])
def get_section(section: str):
    try:
        try:
            return app.send_static_file(f"{section}.html"), 200
        except NotFound:
            return app.send_static_file(f"404.html"), 404
    except:
        logging.exception("Returning HTTP 500:")
        return app.send_static_file(f"500.html"), 500


@app.route("/<folder>/<resource>", methods=["GET"])
def get_static_resource(folder: str, resource: str):
    try:
        try:
            return app.send_static_file(f"{folder}/{resource}"), 200
        except NotFound:
            return "", 404
    except:
        logging.exception("Returning HTTP 500:")
        return app.send_static_file(f"500.html"), 500
