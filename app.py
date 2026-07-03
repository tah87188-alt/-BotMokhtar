from flask import Flask, request
import requests
import openai
import os

app = Flask(name)

OPENAI_KEY = os.environ.get("OPENAI_KEY")
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")

openai.api_key = OPENAI_KEY

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
if request.method == "GET":
if request.args.get("hub.verify_token") == "mokhtar123":
return request.args.get("hub.challenge"), 200
if request.method == "POST":
data = request.get_json()
try:
msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
from_number = msg["from"]
user_text = msg["text"]["body"]

response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[{"role":"user","content":user_text}]
)
reply = response.choices[0].message.content

url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
payload = {"messaging_product":"whatsapp","to":from_number,"text":{"body":reply}}
requests.post(url, headers=headers, json=payload)
except: pass
return "ok"

if name == "main":
app.run()