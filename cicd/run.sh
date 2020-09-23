#!/bin/bash

export FLASK_APP=cicd.py

flask run --port 8089 --host=0.0.0.0
