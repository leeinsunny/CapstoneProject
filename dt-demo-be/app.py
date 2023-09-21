from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import modules.run as modules
import os
import pandas as pd

def mark_from_sentence(sentence, part):
    """
    This function gets 2 arguments to partially mark from given sentence.

    :param sentence: Whole sentence
    :type sentence: string
    :param part: part to mark
    :type part: string

    Sample Parameters:
    - sentence: "게시글 샘플 임니다."
    - part: "임"

    Sample Return:
    "게시글 샘플 <mark>임</mark>니다."
    """
    return sentence.replace(part, f'<mark>{part}</mark>')

def get_details_table_data():
    """
    This function reads demo_details.csv file from ../database path
    and create data to render HTML template.

    Sample return is as follows
    {
        0: {
            '유형': '오탈자',
            '원문': '안녕<mark>흐</mark>세요',
            '변환': '안녕<mark>하</mark>세요',
        },
        1: {
            '유형': '개인정보: 전화번호',
            '원문': '내 번호는 <mark>010-1234-1234</mark>야',
            '변환': '내 번호는 <mark>010-****-****</mark>야',
        },
    }
    """
    db_path = os.path.join("..", "database")
    details_path = os.path.join(db_path, "demo_details.csv")
    df = pd.read_csv(details_path)

    details_data = {}
    
    for index, row in df.iterrows():
        details_data[index] = {
            '유형': row['유형'],
            '원문': mark_from_sentence(row['원문'], row['원문_부분']),
            '변환': mark_from_sentence(row['변환'], row['변환_부분']),
        }
        
    return details_data

################################### API ###################################

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

        # Sample API request body:
        '''
        {
            "form": {
                "all": false,
                "modules": "typo,pdd,slang",
                "input": "demo.txt"
            }
        }
        '''
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

@app.route("/api/filter/filelist", methods=["GET"])
def file_list():
    app.logger.info("API request on upload func: GET")

    # TODO: make arguments for file list
    file_list_sample = ["file1", "file2", "file3", "file4", "new file"]
    return jsonify(file_list_sample)
        

@app.route("/api/filter/report", methods=["GET"])
def get_report():
    template_path = os.path.join("filter_report", "template.html")
    db_path = os.path.join("..","database")

    # TODO: calculate overview_rate according to the file size

    original_fName = "demo.txt"
    converted_fName = "demo_filtered.txt"

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
        'contents_original_fName': original_fName,
        'contents_converted_fName': converted_fName,
        'contents_original': "",
        'contents_converted': "",
        'details': {}
    }
    # update overview_all
    report_data_sample['overview_all'] = report_data_sample['overview_typo'] + report_data_sample['overview_slang'] + report_data_sample['overview_pdd'] + report_data_sample['overview_dup'] + report_data_sample['overview_char']

    # Original contents
    original_fPath = os.path.join(db_path, original_fName)
    contents_original = ""
    with open(original_fPath, 'r', encoding='UTF-8') as file:
        contents_original = file.read()
        contents_original = contents_original.replace("\n", "<br> ")
    report_data_sample['contents_original'] = contents_original

    # Converted contents
    converted_fPath = os.path.join(db_path, converted_fName)
    contents_converted = ""
    with open(converted_fPath, 'r', encoding='UTF-8') as file:
        contents_converted = file.read()
        contents_converted = contents_converted.replace("\n", "<br> ")
    report_data_sample['contents_converted'] = contents_converted

    # Details table
    report_data_sample['details'] =  get_details_table_data()

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