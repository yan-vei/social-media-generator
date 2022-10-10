from backend.src.entities.article import ArticleSchema

def validate_schema(request):
    try:
        article = ArticleSchema() \
            .load(request.get_json())
        return article
    except:
        raise Exception("Invalid article schema")
