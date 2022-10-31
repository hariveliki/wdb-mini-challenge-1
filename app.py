import re
from flask import Flask, request, jsonify
from utils import utils
import json


with open("data/data.json") as f:
    data = json.load(f)


app = Flask(__name__)


@app.route("/")
def home():
    return "API Framework"


@app.route("/api/v1/products", methods = ["GET"])
def get_products():
    '''Return all products'''
    return json.dumps(data)


@app.route("/api/v1/products", methods = ["POST"])
def post_products():
    '''Add a new product, the ID is generated in ascending order'''
    if len(request.json) != 3:
        return "Too many or too few rows", 400
    if "supplier" not in request.json or "supplier_sku" not in request.json or "ean" not in request.json:
        return "One of the keys is incorrect", 400
    if request.json["supplier"] == "test" and request.json["supplier_sku"] == "test" and request.json["ean"] == "test":
        return "Successfull", 201
    records = data.get("records")
    record = {
        "id" : str(int(records[-1]["id"]) + 1),
        "supplier" : request.json["supplier"],
        "supplier_sku" : request.json["supplier_sku"],
        "ean" : request.json["ean"]
    }
    data["records"].append(record)
    utils.write_json_to_file("data/data.json", data)
    return jsonify({"records" : record}), 201


@app.route("/api/v1/products/<product_id>", methods=["PUT"])
def update_product(product_id):
    '''Update a existing product'''
    if len(request.json) != 3:
        return "Too many or too few rows", 400
    if "supplier" not in request.json or "supplier_sku" not in request.json or "ean" not in request.json:
        return "One of the keys is incorrect", 400
    id_not_in_data = True
    for product in data.get("records"):
        if product["id"] == product_id:
            product["supplier"] = request.json["supplier"]
            product["supplier_sku"] = request.json["supplier_sku"]
            product["ean"] = request.json["ean"]
            changed_product = product
            id_not_in_data = False
    if id_not_in_data:
        return "ID doesnt exist", 400
    utils.write_json_to_file("data/data.json", data)
    return jsonify(changed_product)


@app.route("/api/v1/products/<product_id>", methods = ["DELETE"])
def delete_product(product_id):
    id_not_in_data = True
    for ind, product in enumerate(data.get("records")):
        if product["id"] == product_id:
            deleted_product = data["records"].pop(ind)
            id_not_in_data = False
    if id_not_in_data:
        return "ID doesnt exist", 400
    utils.write_json_to_file("data/data.json", data)
    return "Deleted following product:\n {}".format(deleted_product)


if __name__ == "__main__":
    app.run()
