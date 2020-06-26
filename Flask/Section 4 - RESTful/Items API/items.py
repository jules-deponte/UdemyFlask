import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from user import User

from security import authenticate, identity, new_user

app = Flask(__name__)
app.secret_key = 'DouglasDaleDouglas'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []

class ItemList(Resource):
    def get(self):
        pass

class Item(Resource):

    @classmethod
    @jwt_required()    
    def get(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        item_query = "SELECT item, price FROM items WHERE item = ?"
        result = cursor.execute(item_query, (name,))
        row = result.fetchone()
        
        if row:
            item, price = row    
            connection.close()    
            return {'item':item, 'price':price}, 201
        else:
            connection.close()
            return {'message':'Item does not exist'}, 404
                
        

        
    
    @jwt_required()
    def post(cls, name):
        if cls.get(name)[1] == 201:
            return {'message':'This item already exists.'}

        request_data = request.get_json()
        price = request_data['price']
        item = {'name':name, 'price':price}
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        post_item = "INSERT INTO items (item, price) VALUES (?, ?)"
        cursor.execute(post_item, (name, price))
        connection.commit()

        return item, 201, connection.close()

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

