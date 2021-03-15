from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger

from service.customer_service import CarService

from marshmallow import Schema, fields


class CarQuerySchema(Schema):
    id = fields.Int(required=False)

get_schema = CarQuerySchema()

class CarPostSchema(Schema):
    name = fields.String(required=True)

post_schema = CustomerPostSchema()

class CustomerPutSchema(Schema):
    id = fields.Int(required=True)
    name = fields.String(required=True)

put_schema = CustomerPutSchema()

class CustomerDeleteSchema(Schema):
    id = fields.Int(required=True)

delete_schema = CustomerDeleteSchema()



class Customer(Resource):

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
        print(request.json)
        print(request.args)
        errors = get_schema.validate(request.args)

        if errors and bool(request.args):
            query = errors

        elif not bool(request.args):
            query = CustomerService().get_all()
        else:
            _id = request.args['id']
            query = CustomerService().get_by_id(id=_id)

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


    @swagger.operation(
        notes="Update customer info",
        nickname="Update customer",
        # Parameters can be automatically extracted from URLs.
        #   For Example: <string:id>
        # but you could also override them here, or add other parameters.
        parameters=[
            {
                "name": "name",
                "description": "Customer Full name",
                "required": False,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "body",
            },
            {
                "name": "customer_id",
                "description": "Customer ID",
                "required": False,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "body",
            }
        ],
    )

    def put(self):
        print(request.json)
        errors = put_schema.validate(request.json)

        if errors:
            query = errors
        else:
            _id = request.json['id']
            name = request.json['name']
            query = CustomerService().update(id=_id, name=name)

        return query

    @swagger.operation(
        notes="Delete a customer from the database",
        nickname="Delete customer",
        # Parameters can be automatically extracted from URLs.
        #   For Example: <string:id>
        # but you could also override them here, or add other parameters.
        parameters=[
            {
                "name": "name",
                "description": "Customer Full name",
                "required": False,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "body",
            },
            {
                "name": "customer_id",
                "description": "Customer ID",
                "required": False,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "body",
            }
        ],
    )

    def delete(self):
        print(request.json)
        errors = delete_schema.validate(request.json)

        if errors:
            query = errors
        else:
            _id = request.json['id']
            query = CustomerService().delete(id=_id)

        return query
