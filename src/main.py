from flask import Flask, send_file
from config import Config
# import resume_parser

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def hello():
    return send_file("../frontend/index.html")

# @app.route('/read-resume')
# def read_resume():
#     return "Reading the resume"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)