# python flask demo app

from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    hostname = os.uname()[1]
    host = f'<h1>Hello, {hostname}!</h1>'
    ENV = os.getenv('ENV')
    ENV1 = os.getenv('ENV1')
    ENV2 = os.getenv('ENV2')
    env = f'<p>My Environment: {ENV}</p>'
    env1 = f'<p> My Env1: {ENV1}'
    env2 = f'<p> My Env2: {ENV2}'
    return host + env + env1+env2
