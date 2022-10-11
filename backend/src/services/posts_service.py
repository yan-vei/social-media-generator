from backend.src.entities.post import PostSchema


def validate_schema(request):
    try:
        post = PostSchema() \
            .load(request.get_json())
    except:
        raise Exception("Invalid post schema")

    if (post['text_extract_id'] == None and post['article_id'] == None):
        raise Exception("Post doesn't contain neither text_extract_id nor article_id")

    return post