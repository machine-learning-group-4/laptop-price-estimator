
from flask import Blueprint, request, jsonify

# Create a Blueprint for our API routes
api = Blueprint("api", __name__)


# Home endpoint
@api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Laptop Price Estimator API is running!",
        "status": "success"
    }), 200


# Health check endpoint
@api.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "message": "Backend is working correctly"
    }), 200


# Prediction endpoint
@api.route("/predict", methods=["POST"])
def predict():

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "status": "error",
            "error": "Invalid or missing JSON data"
        }), 400

    if not isinstance(data, dict):
        return jsonify({
            "status": "error",
            "error": "Request data must be a JSON object"
        }), 400

    if not data:
        return jsonify({
            "status": "error",
            "error": "No data provided"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Data received successfully",
        "received_data": data,
        "prediction_status": "not_ready"
    }), 200
