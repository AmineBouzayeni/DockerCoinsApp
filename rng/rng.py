from flask import Flask, Response
import os
import socket
import time
from logging.config import dictConfig
from flask.logging import default_handler

app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    },
    'debug': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})



hostname = socket.gethostname()

urandom = os.open("/dev/urandom", os.O_RDONLY)


@app.route("/")
def index():
    app.logger.info("GET - /")
    return "RNG running on {}\n".format(hostname)


@app.route("/<int:how_many_bytes>")
def rng(how_many_bytes):
    # Simulate a little bit of delay
    time.sleep(0.1)
    app.logger.info(f"GET - /{how_many_bytes}")
    return Response(
        os.read(urandom, how_many_bytes),
        content_type="application/octet-stream")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)