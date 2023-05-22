import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)

# GET - Retrieve All Stores and Their Items
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

# GET - Get All Items
@app.get("/item") 
def get_items():
    return {"items": list(items.values())}

# GET - Retrieve a Particular Store
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404

# GET - Retrieve Items from a Store
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try: 
        return items[item_id]
    except KeyError:
        return {"message": "Store not found"}, 404

# POST - Create a Store
@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

# POST - Create an Item
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item, 201

# port 5000 was glitchy - localhost forced to use port 5001
if __name__ == '__main__':
    app.run(debug=True, port=5001)