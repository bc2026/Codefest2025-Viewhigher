from flask import Flask, send_file, send_from_directory
import os

app = Flask(__name__, static_folder="static")

# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    """Serve the index.html file from the src directory"""
    return send_file(os.path.join(BASE_DIR, "index.html"))  # Ensure index.html is inside src/

@app.route('/static/assets/<path:filename>')
def serve_static(filename):
    """Serve static files (images, CSS, etc.)"""
    return send_from_directory(os.path.join(BASE_DIR, "static/assets"), filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
