from flask import Blueprint
from flask import jsonify, make_response, request
from backend.src.controllers import text_extracts_controller
from backend.src.services import text_extracts_service


text_extracts = Blueprint("text_extracts", __name__)


@text_extracts.route('/text-extracts')
def get_text_extracts():
    text_extracts = text_extracts_controller.get_text_extracts()

    return make_response(jsonify(text_extracts), 200)


@text_extracts.route('/text-extracts', methods=['POST'])
def save_text_extract():
    posted_text_extract = text_extracts_service.validate_schema(request)
    new_text_extract = text_extracts_controller.save_text_extract(**posted_text_extract)

    return make_response(jsonify(new_text_extract), 201)


@text_extracts.route('/text-extracts', methods=['DELETE'])
def delete_text_extract():
    id = request.args.get('id')
    text_extracts_controller.delete_text_extract_by_id(id)

    return make_response(jsonify({"status": "success", "message:": "Successfully deleted the text extract with the id " + id}), 200)