from flask import Blueprint, send_file
from flask import jsonify, make_response, request
import os

admin = Blueprint("admin", __name__)


@admin.route('/configs', methods=['GET', 'POST'])
def process_configs():
    cwd = os.getcwd()
    if request.method == 'GET':
        try:
            filename = request.args.get('filename')
            path = cwd + "\\data\\" + filename
            return send_file(path, as_attachment=True)
        except FileNotFoundError:
            return make_response(jsonify({"message": "File not found"}), 404)

    elif request.method == 'POST':
        try:
            file = request.files["file"]
            file.save(os.path.join(cwd + "\\data", file.filename))
            return make_response(jsonify({"message": "Settings have been updated."}), 200)
        except Exception as e:
            return make_response(jsonify({"error": "Something went wrong.", "ex": str(e)}), 500)