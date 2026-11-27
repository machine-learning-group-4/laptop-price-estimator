
from flask import Blueprint, request, jsonify
from validators import validate_prediction_payload

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
    validated_data, error = validate_prediction_payload(data)

    if error:
        return jsonify({
            "status": "error",
            "error": error
        }), 400

    return jsonify({
        "status": "success",
        "message": "Data received successfully",
        "received_data": validated_data,
        "prediction_status": "not_ready"
    }), 200