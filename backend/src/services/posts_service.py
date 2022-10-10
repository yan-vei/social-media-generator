from backend.src.entities.post import PostSchema


def validate_schema(request):
    try:
        post = PostSchema() \
            .load(request.get_json())
        return post
    except:
        raise Exception("Invalid text extract schema")