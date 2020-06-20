from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity, new_user

app = Flask(__name__)
app.secret_key = 'DouglasDaleDouglas'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []

class ItemList(Resource):
    def get(self):
        if items == []:
            return {"items": None}, 404
        return {'items':items}, 200

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'message': item}, 200 if item is not None else 404
    
    @jwt_required()
    def post(self, name):
        if next(filter(lambda item: item['name'] == name, items), None):
            return {'message':f'An item with name {name} already exists.'}, 400

        request_data = request.get_json()
        price = request_data['price']
        item = {'name':name, 'price':price}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message':"Item deleted"}, 200
        # return {'message':'Item does not exist'}, 400

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'price',
            type=float,
            required=True,
            help='This field cannot be blank'
        )
        request_data = parser.parse_args()

        item = next(filter(lambda item: item['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price':request_data['price']}
            items.append(item)
            return {'message':'Item created'}
        else:
            item.update(request_data)
            return {'message':'Item updated'}

class Signup(Resource):
    def post(self):
        request_data = request.get_json()
        username = request_data['username']
        password = request_data['password']
        new_user(username, password)
        return {'message':'User created'}



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Signup, '/signup')

app.run(port=5000, debug=True)