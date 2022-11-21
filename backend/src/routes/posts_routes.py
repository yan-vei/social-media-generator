from flask import Blueprint
from flask import jsonify, make_response, request
from backend.src.controllers import posts_controller

posts = Blueprint("posts", __name__)

@posts.route('/posts-by-article', methods=['GET'])
def get_posts_by_article_id():
    user_token = request.headers['Authorization']

    if user_token == None or user_token == '':
        return make_response(jsonify({'message': 'Unauthorized access. Login first'}), 401)

    posts = posts_controller.get_posts_by_article_id(request.args.get('id'))

    return make_response(jsonify(posts), 200)


@posts.route('/posts-by-text-extract', methods=['GET'])
def get_posts_by_text_extract_id():
    user_token = request.headers['Authorization']

    if user_token == None or user_token == '':
        return make_response(jsonify({'message': 'Unauthorized access. Login first'}), 401)

    posts = posts_controller.get_posts_by_text_extract_id(request.args.get('id'))
    return make_response(jsonify(posts), 200)

@posts.route('/posts', methods=['DELETE'])
def delete_post():
    try:
        id = request.args.get('id')
        posts_controller.delete_post_by_id(id)

        return make_response(jsonify({"status": "success", "message:": "Successfully deleted the post with the id " + id}), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 500)