from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/carts', methods=['GET'])
def get_carts():
    # Query the database for all available carts
    # Return the carts in JSON format
    return 

@app.route('/carts/create', methods=['POST'])
def create_cart():
    # Accept building_id from the request body to create a new cart
    # Add the cart to the database
    # Return the updated list of carts in JSON format
    building_id = request.json.get('building_id')
    return 

@app.route('/carts/<int:cart_id>', methods=['GET'])
def get_cart_items(cart_id):
    # Query the database for items in the specified cart
    # Return the items and cart details in JSON format
    return 

@app.route('/carts/<int:cart_id>/add/<int:item_id>', methods=['PUT'])
def add_to_cart(cart_id, item_id):
    # Check if the cart exists and add the specified item
    # Return the updated cart in JSON format
    return 

@app.route('/carts/<int:cart_id>/remove/<int:item_id>', methods=['PUT'])
def remove_from_cart(cart_id, item_id):
    # Check if the cart exists and remove the specified item
    # Return the updated cart in JSON format
    return 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)