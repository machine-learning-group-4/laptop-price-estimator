
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow frontend applications to communicate with the backend
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Laptop Price Estimator API is running!"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data provided"
        }), 400

    return jsonify({
        "message": "Laptop specifications received successfully",
        "received_data": data
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
