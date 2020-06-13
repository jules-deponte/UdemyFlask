from flask import Flask

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

# POST /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    pass

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def post_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

# Home
@app.route('/')
def home():
    return '<h1>it worked</h1>'


app.run()