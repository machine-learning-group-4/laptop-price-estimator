def validate_prediction_payload(data):
    if data is None:
        return None, "Invalid or missing JSON data"

    if not isinstance(data, dict):
        return None, "Request data must be a JSON object"

    if not data:
        return None, "No data provided"

    return data, None