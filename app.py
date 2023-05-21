from flask import Flask, request

app = Flask(__name__)

# Sample/Default data
stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

# GET - Retrieve All Stores and Their Items
@app.get("/store")
def get_stores():
    return {"stores": stores}

# GET - Retrieve a Particular Store
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

# GET - Retrieve Items from a Store
@app.get("/store/<string:name>/item")
def get_item(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404

# POST - Create a Store
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

# POST - Create an Item
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

# port 5000 was glitchy - localhost forced to use port 5001
if __name__ == '__main__':
    app.run(debug=True, port=5001)