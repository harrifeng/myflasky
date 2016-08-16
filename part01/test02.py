from flask import Flask
from flask import request
from flask import current_app
app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/appname')
def user():
    name = current_app.name
    return '<h1>Hello %s</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
