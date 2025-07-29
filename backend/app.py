import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Backend Flask API!"

if __name__ == '__main__':
    # Run only if not in CI
    if os.getenv("CI") != "true":
        app.run(host='0.0.0.0', port=5000)

