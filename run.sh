#!/bin/bash
export FLASK_APP=src/controller.py
flask run --port 80 --host=0.0.0.0
