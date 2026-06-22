from flask import Flask, jsonify
from threading import Thread
import os

app = Flask('')

bot_status = {
    "discord_online": False,
    "telegram_online": False
}

@app.route('/')
def home():
    return "Matrix Bridge Engine is Operational.", 200

@app.route('/status')
def status():
    return jsonify(bot_status), 200

def run():
    # Render and livemy.app pass a dynamic port via environment variables
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
