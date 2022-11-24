from flask import Flask

app = Flask(__name__)


def get_html_data():
    return """<div style="display: flex;
    justify-content: center;
    align-items: center;"><h2>Hello, World!</h2></div>"""


@app.route("/")
def hello_world():
    return get_html_data()
