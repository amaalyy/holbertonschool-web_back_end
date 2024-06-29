# Import the Flask module
from flask import Flask, jsonify

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def welcome():
    """Route handler for the root URL."""
    # Return a JSON payload with a welcome message
    return jsonify({"message": "Bienvenue"})

# Run the Flask app if the script is executed directly
if __name__ == "__main__":
    # Start the Flask development server
    app.run(host="0.0.0.0", port=5000)
