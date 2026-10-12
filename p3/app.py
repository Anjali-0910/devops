# Import the Flask class
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return "Hello from a Dockerized Flask application!"

# Define a second route
@app.route("/about")
def about():
    return "This Flask app is running inside a Docker container."

# Run the app on all network interfaces so Docker can expose it
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
