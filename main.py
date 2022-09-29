from flask import Flask, request, jsonify 
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "First API call"


with open("api_data.json") as f:
    data = json.load(f)


@app.route("/api/v1/resources/books/all", methods = ["GET"])
def api_all():
    return json.dumps(data)


@app.route("/post", methods=["POST"])
def test_post():
    input_json = request.get_json(force=True)
    dictToReturn = {"text" : input_json["text"]}
    return jsonify(dictToReturn)


app.run()