from flask import Blueprint
from flask import jsonify, make_response, request
from backend.src.controllers import  hashtags_controller

hashtags = Blueprint("hashtags", __name__)

@hashtags.route('/hashtags')
def get_posts():
    try:
        posts = hashtags_controller.get_hashtags()

        return make_response(jsonify(posts), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 500)

@hashtags.route('/hashtags', methods=['DELETE'])
def delete_post():
    try:
        id = request.args.get('id')
        hashtags_controller.delete_hashtag_by_id(id)

        return make_response(jsonify({"status": "success", "message:": "Successfully deleted the post with the id " + id}), 200)

    except Exception as e:
        return make_response(jsonify({"message": e, "status": "failed"}), 500)