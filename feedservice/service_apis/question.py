from flask import request
from flask_restful import Resource


class Question(Resource):
    def get(self):
        data = request.get_json()

        pass
    def post(self):
        pass
    def put(self):
        pass