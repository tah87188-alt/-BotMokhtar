from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Live ✅"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # ده عشان Meta تتأكد من الويب هوك
        return "webhook ok", 200
    
    if request.method == "POST":
        data = request.get_json()
        print("Received:", data)
        return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
