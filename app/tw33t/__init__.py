
from flask import Flask, app
import sys

app = Flask(__name__)
application = app

# Setup the app with the config.py file
app.config.from_object('config')
from tw33t.views import main
