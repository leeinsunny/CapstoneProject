from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import modules.run as modules
import os

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

@app.route("/api/filter/report", methods=["GET"])
def get_report():
    template_path = os.path.join("filter_report", "template.html")
    
    # TODO: calculate overview_rate according to the file size

    report_data_sample = {
        'title': "Report",
        'title_fileName': "demo.txt",
        'overview_rate': "10%",
        'overview_typo': 5,
        'overview_slang': 3,
        'overview_pdd': 2,
        'overview_dup': 4,
        'overview_char': 6,
        'overview_all': 0,
        'contents_original_fName': "original.txt",
        'contents_converted_fName': "converted.txt",
        'contents_original': "This is the original content.",
        'contents_converted': "This is the converted content.",
        'details': {}
    }
    # update overview_all
    report_data_sample['overview_all'] = report_data_sample['overview_typo'] + report_data_sample['overview_slang'] + report_data_sample['overview_pdd'] + report_data_sample['overview_dup'] + report_data_sample['overview_char']

    details_sample = {
        1: {
            '유형': '오탈자',
            '원문': '안녕<mark>흐</mark>세요',
            '변환': '안녕<mark>하</mark>세요',
        },
        2: {
            '유형': '개인정보: 전화번호',
            '원문': '내 번호는 <mark>010-1234-1234</mark>야',
            '변환': '내 번호는 <mark>010-****-****</mark>야',
        },
    }
    report_data_sample['details'] = details_sample

    return render_template(template_path, **report_data_sample)

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