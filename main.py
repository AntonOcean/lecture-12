from flask import Flask

app = Flask(__name__)


def get_html_data():
    return """<h2>Hello, World!</h2>"""


@app.route("/")
def hello_world():
    return get_html_data()
