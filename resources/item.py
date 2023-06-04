import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema


blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    # GET - Retrieve Specific Item
    def get(self, item_id):
        try: 
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    # DELETE - Delete an Item
    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item was successfully deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    # UPDATE - Update an Item
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):

    # GET - Get All Items
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    # POST - Create an Item
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data): 
        item = ItemModel(**item_data)

        try: 
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item