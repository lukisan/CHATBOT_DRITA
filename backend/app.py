from flask import Flask
from flask import jsonify
from flask import request
import json
from flask_cors import CORS
from demo import initial_message, zero_chat

app = Flask(__name__)
app.run(debug=True)
CORS(app)

@app.route('/', methods=['GET'])
def getMessage():
    return jsonify({"message": initial_message()})

@app.route('/message', methods=['POST'])
def createMessage():
    req_data = request.get_json()
    resp = zero_chat(req_data["message"])
    return jsonify({"message": resp})