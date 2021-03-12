from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger

from service.customer_service import CustomerService
from service.car_service import CarService

from marshmallow import Schema, fields


class CarByCustomerGetSchema(Schema):
    id = fields.Int(required=False)

get_schema = CarByCustomerGetSchema()

class CarByCustomerPostSchema(Schema):
    name = fields.String(required=True)

post_schema = CarByCustomerPostSchema()


class CarByCustomer(Resource):

    @swagger.operation(
        notes="Read a customer from the database",
        nickname="Read customer",
        # Parameters can be automatically extracted from URLs.
        #   For Example: <string:id>
        # but you could also override them here, or add other parameters.
        parameters=[
            {
                "name": "id",
                "description": "Customer ID",
                "required": False,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "body",
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Sucess",
                "response": {"name": "John Wick",
                             "customer_id": 123123,
                             "sale_opportunity": False,
                             "cars": [{"car_id": 321321,
                                       "model": "sedan",
                                       "color": "gray"}]}
            },
            {"code": 405, "message": "Invalid input"},
        ]
    )

    def get(self):
        errors = get_schema.validate(request.args)

        if errors and bool(request.args):
            query = errors
        else:
            _id = request.args['id']
            if _id:
                query = CarService().get_cars_from_customer(_id)
            else:
                query = CarService().get_all_cars_and_customers()

        return query

    
    @swagger.operation(
        notes="Add a customer",
        nickname="Add customer",
        parameters=[
            {
                "name": "name",
                "description": "Customer Full name",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "body",
            },
        ],
        responseMessages=[
            {
                "code": 201,
                "message": "Created. The URL of the created blueprint should "
                + "be in the Location header",
            },
            {"code": 405, "message": "Invalid input"},
        ],
    )


    def post(self):
        print(request.json)
        errors = post_schema.validate(request.json)

        if errors:
            query = errors
        else:
            name = request.json['name']
            query = CustomerService().create(name=name)

        return query
