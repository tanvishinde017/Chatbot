from flask import Flask, render_template, request, jsonify
import logging

from backend.model import get_response
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_reply = get_response(user_message)

    logging.info(f"User: {user_message} | Bot: {bot_reply}")

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
