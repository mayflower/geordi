#!/bin/bash
# Required to run: python, virtualenv, git
virtualenv .env
.env/bin/pip install -r requirements.txt
. .env/bin/activate
