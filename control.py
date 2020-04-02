from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data = {}


def get_todo_container():
    return data


def set_todo_container(data):
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
api.add_resource(DataRequests, '/data/<string:data_id>')
api.add_resource(DataGetter, '/data')


if __name__ == '__main__':
    app.run(debug=True)