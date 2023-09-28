from flask import Flask, jsonify, request
from flask_cors import CORS
import modules.run as modules

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/filter", methods=['GET', 'POST'])
def filter():
    if request.method == 'GET':
        app.logger.info("API request on filtering func: GET")
        data = {'data': 'Hi, this is filter request(GET) from Flask server.'}
        response = jsonify(data)
        response.headers['Content-Type'] = 'application/json'
        return response
    elif request.method == 'POST':
        app.logger.info("API request on filtering func: POST")

        data = request.get_json()
        args = modules.argparse.Namespace(
            all=data['form']['all'],
            modules=data['form']['modules'],
            input=data['form']['input']
        )

        app.logger.info(f"arguments: all={args.all}, modules={args.modules}, input={args.input}")
        modules.runModule(args)
        return "Filtering Requested"
    else:
        return "Unexpected API request"

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