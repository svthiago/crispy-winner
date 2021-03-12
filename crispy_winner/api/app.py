from flask import Flask
from flask_restful import reqparse, abort, Api
from flask_restful_swagger import swagger

from routes.customer import Customer
from routes.car_by_customer_api import CarByCustomer


app = Flask(__name__)
api = Api(app)

api.add_resource(Customer, '/customer')
api.add_resource(CarByCustomer, '/car_by_customer')


if __name__ == '__main__':
    app.run()
