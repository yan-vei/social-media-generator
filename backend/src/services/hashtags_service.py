from backend.src.entities.hashtag import HashtagSchema


def validate_schema(request):
    try:
        hashtag = HashtagSchema() \
            .load(request.get_json())
    except:
        raise Exception("Invalid hashtag schema")

    if (hashtag['text_extract_id'] == None and hashtag['article_id'] == None):
        raise Exception("Hashtag doesn't contain neither text_extract_id nor article_id")

    return hashtag