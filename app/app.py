import os

from flask import Flask, jsonify

app = Flask(__name__)

# set at deploy time so we can see which build is running
VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/")
def home():
    return "Hello from the CI/CD demo app"


@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION)


if __name__ == "__main__":
    # 0.0.0.0 so the app is reachable from outside the container
    app.run(host="0.0.0.0", port=5000)

