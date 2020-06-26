from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from user import User, Signup

from security import authenticate, identity, new_user

import items

app = Flask(__name__)
app.secret_key = 'DouglasDaleDouglas'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(items.Item, '/item/<string:name>')
api.add_resource(items.ItemList, '/items')
api.add_resource(Signup, '/signup')

app.run(port=5000, debug=True)