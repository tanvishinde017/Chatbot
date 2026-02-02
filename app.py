from flask import Flask, render_template, request, jsonify
from backend.model import get_response

app = Flask(__name__)

chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_message = get_response(user_message)

    chat_history.append({
        "user": user_message,
        "bot": bot_message
    })

    return jsonify({
        "reply": bot_message,
        "history": chat_history
    })

if __name__ == "__main__":
    app.run(debug=True)
