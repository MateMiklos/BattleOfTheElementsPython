from flask import Flask, request
from flask_restful import Resource, Api

import engine
import data_handler

app = Flask(__name__)
api = Api(app)

game = engine.game()
data = data_handler.create_json_data(game)


def get_data_container():
    return data


def set_data_container(data):
    data = data
    return data


class DataRequests(Resource):
    def get(self, data_id):
        return {data_id: data[data_id]}

    def put(self, data_id):
        data[data_id] = request.form['data']
        return {data_id: data[data_id]}


class DataGetter(Resource):
    def get(self):
        return data


# Adding the routes
api.add_resource(DataRequests, '/game/<string:data_id>')
api.add_resource(DataGetter, '/game')


if __name__ == '__main__':
    app.run(debug=True)
