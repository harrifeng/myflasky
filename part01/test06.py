from flask import Flask
from flask import abort
app = Flask(__name__)


@app.route('/')
def index():
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
