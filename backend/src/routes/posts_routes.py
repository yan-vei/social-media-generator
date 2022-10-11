from flask import Blueprint
from flask import jsonify, make_response, request
from backend.src.controllers import posts_controller
from backend.src.services import posts_service

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


@posts.route('/posts', methods=['POST'])
def save_post():
    try:
        posted_post = posts_service.validate_schema(request)
        new_post = posts_controller.save_post(**posted_post)

        return make_response(jsonify(new_post), 201)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 400)