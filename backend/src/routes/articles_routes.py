from flask import Blueprint
from flask import jsonify, make_response, request
from backend.src.controllers import articles_controller
from backend.src.services import articles_service

articles = Blueprint("articles", __name__)

@articles.route('/articles')
def get_articles():
    articles = articles_controller.get_articles()

    return jsonify(articles)


@articles.route('/articles', methods=['DELETE'])
def delete_article():
    id = request.args.get('id')
    articles_controller.delete_article_by_id(id)

    return(jsonify("Successfully deleted the article with the id " + id), 200)


@articles.route('/articles', methods=['POST'])
def save_article():
    posted_article = articles_service.validate_schema(request)
    new_article = articles_controller.save_article(**posted_article)

    return jsonify(new_article), 201