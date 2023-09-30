from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from det_report import DetReport
import dbconn

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# TODO: Design where to store did value for current user process
did = 1

@app.route("/api/filter/detreport", methods=["GET"])
def get_det_report():
    detReport = DetReport(app, did)

    db_conn = dbconn.connect_to_db()
    detReport.fetchDetReportInfo(db_conn)
    db_conn.close()

    return detReport.getDetReportInfo()

if __name__ == '__main__':
    app.run(port='5001', debug=True)