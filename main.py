import config
import constants
import decorators

from http import HTTPStatus
from flask import Flask, jsonify, request

app = Flask(__name__)

logger = config.setup_logger()


@decorators.log(logger, constants.SQUARE)
def square(number):
    value = int(number)

    return value ** 2


def get_message(name):
    return "Hello " + name


@app.route("/", methods=["POST"])
def message():
    data = request.json

    try:
        logger.debug('Data received: {}'.format(data))
        message = get_message(data['name'])
        logger.debug('Message: {}'.format(message))
    except TypeError as err:
        logger.error('Error: {}'.format(err))

        return jsonify(message="You didn't send name.")

    return jsonify(message=message)


@app.route("/square", methods=["POST"])
def hello():
    data = request.json

    try:
        number = data['number']
        result = square(number)
    except Exception:
        return jsonify(message="Invalid Payload."), HTTPStatus.BAD_REQUEST

    return jsonify(result=result)
