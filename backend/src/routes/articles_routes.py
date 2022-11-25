from flask import Blueprint
from flask import jsonify, make_response, request
from controllers import articles_controller, posts_controller, hashtags_controller, articles_extracts_users_controller
from services import articles_service

articles = Blueprint("articles", __name__)

@articles.route('/all-articles')
def get_all_articles():
    articles = articles_controller.get_articles()

    return make_response(jsonify(articles), 200)

@articles.route('/articles', methods=['DELETE'])
def delete_article():
    try:
        id = request.args.get('id')
        posts_controller.delete_posts_by_article_id(id)
        hashtags_controller.delete_hashtags_by_article_id(id)
        articles_extracts_users_controller.delete_by_article_id(id)
        articles_controller.delete_article_by_id(id)

        return make_response(jsonify({"status": "success", "message:": "Successfully deleted the article with the id " + id}), 200)

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