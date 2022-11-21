from flask import Blueprint
from flask import jsonify, make_response, request
from backend.src.controllers import articles_controller
from backend.src.services import articles_service

articles = Blueprint("articles", __name__)

@articles.route('/articles', methods=['DELETE'])
def delete_article():
    try:
        id = request.args.get('id')
        articles_controller.delete_article_by_id(id)

        return make_response(jsonify({"status": "success", "message:": "Successfully deleted the text extract with the id " + id}), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 500)

@articles.route('/articles', methods=['POST'])
def save_article():
    try:
        posted_article = articles_service.validate_schema(request)
        new_article = articles_controller.save_article(**posted_article)

        return make_response(jsonify(new_article), 201)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 400)