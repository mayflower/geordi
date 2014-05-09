"""
WSGI config for project.
"""
import os
import sys

PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, PATH)

activate_this = os.path.join(PATH, '.env/bin/activate_this.py')

if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

from app import app as application