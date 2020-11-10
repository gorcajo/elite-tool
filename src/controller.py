import json
import logging

from flask import Flask
from flask import redirect
from flask import request
from flask import make_response
from flask import send_from_directory

from flask_injector import FlaskInjector
from injector import inject

from werkzeug.exceptions import NotFound

from service import RepairmentsService
from dependencies import configure


logging.basicConfig(
    format="%(levelname).4s | %(asctime)s.%(msecs)03d | %(threadName)-12s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO)

app = Flask(__name__)


# ---------------- back-end ----------------

@inject
@app.route("/api/repairments", methods=["POST"])
def post_repairment(service: RepairmentsService):
    try:
        return json.dumps(service.create_new_repairment(request.json)), 200
    except:
        logging.exception("Returning HTTP 500:")
        return "", 500


@inject
@app.route("/api/repairments", methods=["GET"])
def get_repairments(service: RepairmentsService):
    try:
        return json.dumps(service.get_repairments(request.args)), 200
    except:
        logging.exception("Returning HTTP 500:")
        return "", 500


@inject
@app.route("/api/repairments/<id>", methods=["GET"])
def get_repairment(service: RepairmentsService, id: int):
    try:
        result = service.get_repairment(id)

        if result is not None:
            return json.dumps(result), 200
        else:
            return "", 404
    except:
        logging.exception("Returning HTTP 500:")
        return "", 500


@inject
@app.route("/api/repairments/<id>", methods=["PUT"])
def put_repairment(service: RepairmentsService, id: int):
    try:
        service.modify_repairment(id, request.json)
        return "", 204
    except:
        logging.exception("Returning HTTP 500:")
        return "", 500


@inject
@app.route("/api/repairments/<id>", methods=["DELETE"])
def delete_repairment(service: RepairmentsService, id: int):
    try:
        service.delete_repairment(id)
        return "", 204
    except:
        logging.exception("Returning HTTP 500:")
        return "", 500


# ---------------- files ----------------

@app.route("/files/repairment-<id>.pdf", methods=["GET"])
def get_repairment_pdf(service: RepairmentsService, id: int):
    try:
        pdf = service.get_repairment_pdf(id)

        if pdf is not None:
            response = make_response(pdf)
            response.headers.set("Content-Type", "application/pdf")
            return response
        else:
            return redirect("/pages/404", code=302)
    except:
        logging.exception("Returning HTTP 500:")
        return "", 500


# ---------------- front-end ----------------

@app.route("/", methods=["GET"])
def get_root():
    return redirect("/pages/browse", code=302)


@app.route("/pages", methods=["GET"])
def get_pages():
    return redirect("/pages/browse", code=302)


@app.route("/pages/<page>", methods=["GET"])
def get_page(page: str):
    try:
        try:
            return app.send_static_file(page + ".html"), 200
        except NotFound:
            return app.send_static_file("404.html"), 404
    except:
        logging.exception("Returning HTTP 500:")
        return app.send_static_file("500.html"), 500


@app.route("/pages/<folder>/<resource>", methods=["GET"])
def get_static_resource(folder: str, resource: str):
    try:
        try:
            return app.send_static_file(folder + "/" + resource), 200
        except NotFound:
            return "", 404
    except:
        logging.exception("Returning HTTP 500:")
        return app.send_static_file("500.html"), 500

FlaskInjector(app=app, modules=[configure])
