import requests
import time
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def measure_latency():
    url = request.args.get('url', '')
    if not url:
        return "URL parameter is missing."

    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    latency = end_time - start_time
    return f"Response latency for {url}: {latency} seconds"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
