from flask import Blueprint, send_file
from flask import jsonify, make_response, request
import os

admin = Blueprint("admin", __name__)


@admin.route('/shortenings', methods=['GET', 'POST'])
def process_shortenings():
    cwd = os.getcwd()
    if request.method == 'GET':
        try:
            path = cwd + "\\data\\shortenings.json"
            return send_file(path, as_attachment=True)
        except FileNotFoundError:
            return make_response(jsonify({"message": "File not found"}), 404)

    elif request.method == 'POST':
        try:
            shortenings = request.files["file"]
            shortenings.save(os.path.join(cwd + "\\data", shortenings.filename))
            return make_response(jsonify({"message": "Settings have been updated."}), 200)
        except Exception:
            return make_response(jsonify({"error": "Something went wrong."}), 500)