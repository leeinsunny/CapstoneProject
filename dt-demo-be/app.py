from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/filter")
def filter():
    data = {'data': 'Hi, this is filter request from Flask server.'}
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/api/converter")
def converter():
    data = {'data': 'Hi, this is converter request from Flask server.'}
    return jsonify(data)

@app.route("/api/statistics")
def statistics():
    data = {'data': 'Hi, this is statistics request from Flask server.'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port='5001', debug=True)