from flask import Flask
from flask.ext.script import Manager
app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    manager.run()
