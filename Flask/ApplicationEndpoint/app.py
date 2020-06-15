from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name':'My Wonderful Store',
        'items':[
            {
                'name':'my item',
                'price':15.99
            }
        ]
    }
]

# POST - used to receive data
# GET - used to send data

# POST /store data {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def post_item_in_store(name):
    request_data = request.get_json() 
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    
    return jsonify({'message':'No store found'})

# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    # Iterate over store
    # If matches, return it
    # If no matches, return an error
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    
    return jsonify({'message':'No store found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    
    return jsonify({'message':'No store found'})


# Home
@app.route('/')
def home():
    return render_template('index.html')


app.run()