##
# Register Controller
#
from pprint import pprint

from flask import request, make_response, jsonify, abort
from flask_restful import Resource


class RegisterController(Resource):
    def post(self):
        pprint(request)
