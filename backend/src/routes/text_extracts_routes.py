from flask import Blueprint
from flask import jsonify, make_response, request
from controllers import text_extracts_controller, posts_controller, hashtags_controller, articles_extracts_users_controller
from services import text_extracts_service


text_extracts = Blueprint("text_extracts", __name__)


@text_extracts.route('/all-text-extracts')
def get_text_extracts():
    text_extracts = text_extracts_controller.get_text_extracts()

    return make_response(jsonify(text_extracts), 200)


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
        posts_controller.delete_posts_by_text_extract_id(id)
        hashtags_controller.delete_hashtags_by_text_extract_id(id)
        articles_extracts_users_controller.delete_by_text_extract_id(id)
        text_extracts_controller.delete_text_extract_by_id(id)

        return make_response(jsonify({"status": "success", "message:": "Successfully deleted the text extract with the id " + id}), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "Failed."}), 500)


@text_extracts.route('/text-extracts-by-title')
def get_article_by_title():
    try:
        title = request.args.get('title')
        texts = text_extracts_controller.get_text_extracts_by_title(title)

        return make_response(jsonify(texts), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "Failed."}), 500)