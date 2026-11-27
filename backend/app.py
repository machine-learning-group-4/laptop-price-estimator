
from flask import Flask
from flask_cors import CORS

from routes import api


# Initialize Flask application
app = Flask(__name__)

# Enable frontend communication
CORS(app)

# Register our API routes
app.register_blueprint(api)


# Run the application
if __name__ == "__main__":
    app.run(debug=True, port=5000)
