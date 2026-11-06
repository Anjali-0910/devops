from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from a Dockerized Flask App!"

if __name__ == "__main__":
    # host="0.0.0.0" makes the server accessible outside the container
    app.run(host="0.0.0.0", port=5000)
