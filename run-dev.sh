#!/bin/bash

export FLASK_APP=controller.py
export FLASK_DEBUG=1

flask run --port 8080
