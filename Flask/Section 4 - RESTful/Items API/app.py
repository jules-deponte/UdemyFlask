from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class ItemList(Resource):
    def get(self):
        if items == []:
            return {"items": None}, 404
        return {'items':items}, 200

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item 
        return {'message': 'Item not found'}, 404
    
    def post(self, name):
        request_data = request.get_json()
        price = request_data['price']
        item = {'name':name, 'price':price}
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)