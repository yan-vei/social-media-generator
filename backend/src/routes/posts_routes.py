from flask import Blueprint
from flask import jsonify, make_response, request
from backend.src.controllers import posts_controller

posts = Blueprint("posts", __name__)

@posts.route('/posts')
def get_posts():
    try:
        posts = posts_controller.get_posts()

        return make_response(jsonify(posts), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 500)

@posts.route('/posts', methods=['DELETE'])
def delete_post():
    try:
        id = request.args.get('id')
        posts_controller.delete_post_by_id(id)

        return make_response(jsonify({"status": "success", "message:": "Successfully deleted the post with the id " + id}), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 500)