from flask import Flask
import redis
import os
import socket

app = Flask(__name__)

# Connect to redis service named 'redis-db'
r = redis.Redis(host='redis-db', port=6379, decode_responses=True)

@app.route('/')
def hello():
    try:
        count = r.incr('hits')
        # We changed the HTML here for v2 👇
        return f"<h1>Phase 1 App (v2)</h1><p>UPDATED VERSION</p><br>Visits: {count}"
    except redis.ConnectionError:
        # We changed the HTML here too 👇
        return "<h1>Phase 1 App (v2)</h1><p>UPDATED VERSION</p><br>Redis is not reachable yet."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)