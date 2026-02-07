from flask import Flask, jsonify
from flask_cors import CORS
from robtop_client import RobTopClient

app = Flask(__name__)
CORS(app)  # allow frontend to communicate

client = RobTopClient()


@app.route("/")
def home():
    return jsonify({"message": "RobTop API Server Running"})


@app.route("/api/profile/<account_id>")
def get_profile(account_id):
    try:
        user = client.get_user_info(account_id)
        return jsonify(user)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

