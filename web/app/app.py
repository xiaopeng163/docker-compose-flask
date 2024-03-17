import os
import socket

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    hits = redis.get('hits').decode('utf-8')
    hostname = socket.gethostname()
    return f"""
    <html>
        <body>
            <h1>Hello Container World!</h1>
            <p>I have been seen <span style="font-size:2em;">{hits}</span> times and my hostname is <span style="font-size:2em;">{hostname}</span>.</p>
        </body>
    </html>
    """
