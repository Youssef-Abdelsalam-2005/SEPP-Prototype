from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB_FILE = "db.json"


def load_db():
    """Load data from the JSON file."""
    with open(DB_FILE, "r") as file:
        return json.load(file)


def save_db(data):
    """Save data to the JSON file."""
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


@app.route('/carts', methods=['GET'])
def get_carts():
    db = load_db()
    return jsonify(db.get("carts", []))


@app.route('/carts/create', methods=['POST'])
def create_cart():
    db = load_db()
    carts = db.setdefault("carts", [])
    data = request.get_json()
    building_id = data.get("building_id")

    if not building_id:
        return jsonify({"error": "building_id is required"}), 400

    new_cart = {"cart_id": len(carts) + 1, "building_id": building_id,       "items": [
        {
          "item_id": 1,
          "name": "Chicken",
          "quantity": 12,
          "price": 10
        },
        {
          "item_id": 2,
          "name": "Beef",
          "quantity": 5,
          "price": 10
        },
        {
          "item_id": 3,
          "name": "Cheese",
          "quantity": 3,
          "price": 10
        },
        {
          "item_id": 4,
          "name": "Juice",
          "quantity": 10,
          "price": 5
        },
        {
          "item_id": 5,
          "name": "Milk",
          "quantity": 8,
          "price": 4
        },
        {
          "item_id": 6,
          "name": "Bread",
          "quantity": 15,
          "price": 3
        }
      ], "cart": [], "time": datetime.utcnow().isoformat()}
    carts.append(new_cart)
    save_db(db)
    return jsonify(new_cart), 201


@app.route('/carts/<int:cart_id>', methods=['GET'])
def get_cart_items(cart_id):
    db = load_db()
    carts = db.get("carts", [])
    cart = next((cart for cart in carts if cart["cart_id"] == cart_id), None)
    if not cart:
        return jsonify({"error": "Cart not found"}), 404
    return jsonify(cart)


@app.route('/carts/<int:cart_id>/add/<int:item_id>', methods=['PUT'])
def add_to_cart(cart_id, item_id):
    db = load_db()
    carts = db.get("carts", [])
    cart = next((cart for cart in carts if cart["cart_id"] == cart_id), None)
    if not cart:
        return jsonify({"error": "Cart not found"}), 404

    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "username is required"}), 400

    item = next((item for item in cart["items"] if item["item_id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found in available items"}), 404

    # Update the cart with the item
    new_item = {**item, "username": username}
    cart["cart"].append(new_item)
    save_db(db)
    return jsonify(cart)


@app.route('/carts/<int:cart_id>/remove/<int:item_id>', methods=['PUT'])
def remove_from_cart(cart_id, item_id):
    db = load_db()
    carts = db.get("carts", [])
    cart = next((cart for cart in carts if cart["cart_id"] == cart_id), None)
    if not cart:
        return jsonify({"error": "Cart not found"}), 404

    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "username is required"}), 400

    # Find and remove the item
    item = next((item for item in cart["cart"] if item["item_id"] == item_id and item["username"] == username), None)
    if not item:
        return jsonify({"error": "Item not found in the cart"}), 404

    cart["cart"].remove(item)
    save_db(db)
    return jsonify(cart)


if __name__ == '__main__':
    # Initialize db.json with default structure if it doesn't exist
    try:
        with open(DB_FILE, "r") as file:
            pass
    except FileNotFoundError:
        with open(DB_FILE, "w") as file:
            json.dump({"carts": []}, file, indent=4)
    app.run(host='0.0.0.0', port=5000)
