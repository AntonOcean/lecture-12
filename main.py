from urllib.parse import unquote

from flask import Flask, request

app = Flask(__name__)

store = []


def new_div_block(data):
    return f"""<div>{data}</div>"""


def get_html_data():
    return """<h2>Hello, World!</h2>"""


def make_chat():
    return "".join([new_div_block(f"{ip}: {data}") for ip, data in store])


@app.route("/")
def hello_world():
    ip = request.remote_addr
    data = unquote(request.query_string.decode("utf-8"))
    if data:
        store.append((ip, data))

    return get_html_data() + make_chat()
