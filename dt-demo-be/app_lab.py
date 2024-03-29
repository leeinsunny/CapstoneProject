from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from document import Document
import dbconn

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# TODO: Design document handling flow
did = 1
test_doc = Document(app, did)

@app.route("/api/filter/detreport", methods=["GET"])
def get_det_report():

    db_conn = dbconn.connect_to_db()
    test_doc.fetchDetReportInfo(db_conn)
    db_conn.close()

    return test_doc.getDetReportInfo()

if __name__ == '__main__':
    app.run(port='5001', debug=True)