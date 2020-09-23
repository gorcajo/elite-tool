#!/usr/bin/env python3.6

import logging
import subprocess

from flask import Flask


logging.basicConfig(
    format="%(levelname).4s | %(asctime)s.%(msecs)03d | %(threadName)-12s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO)

app = Flask(__name__)


@app.route("/cicd", methods=["POST"])
def cicd():
    try:
        # 1. Parar el server

        logging.debug("Stopping server...")

        # TODO

        # 2. Hacer pull del repo
        
        logging.debug("Pulling code from GitHub...")

        subprocess.call(["git", "pull"], cwd="..")

        # 3. Arrancar el server

        logging.debug("Running server...")

        # TODO

        logging.debug("... done")

        return "", 204

    except:
        logging.exception("Returning HTTP 500:")
        return "", 500

