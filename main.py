import logging

from flask import Flask, jsonify, request

app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)


def get_message(name):
    return "Hello " + name


@app.route("/", methods=["POST"])
def hello():
    data = request.json

    try:
        logging.debug('Data received: {}'.format(data))
        message = get_message(data['name'])
        logging.debug('Message: {}'.format(message))
    except TypeError as err:
        logging.error('Error: {err}'.format(err=err))

        return jsonify(message="You didn't send name.")

    return jsonify(message=message)
