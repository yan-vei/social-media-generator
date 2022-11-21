from flask import Blueprint
from flask import jsonify, make_response, request
from backend.src.controllers import text_extracts_controller
from backend.src.services import text_extracts_service


text_extracts = Blueprint("text_extracts", __name__)


@text_extracts.route('/text-extracts', methods=['POST'])
def save_text_extract():
    try:
        posted_text_extract = text_extracts_service.validate_schema(request)
        new_text_extract = text_extracts_controller.save_text_extract(**posted_text_extract)

        return make_response(jsonify(new_text_extract), 201)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 400)


@text_extracts.route('/text-extracts', methods=['DELETE'])
def delete_text_extract():
    try:
        id = request.args.get('id')
        text_extracts_controller.delete_text_extract_by_id(id)

        return make_response(jsonify({"status": "success", "message:": "Successfully deleted the text extract with the id " + id}), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 500)