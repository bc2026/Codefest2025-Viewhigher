from flask import Flask, send_file
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def hello():
    return send_file("index.html")


# @app.route('/read-resume')


if __name__ == '__main__':
    app.run(debug=True)