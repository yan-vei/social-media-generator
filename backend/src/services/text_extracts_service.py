from backend.src.entities.text_extract import TextExtractSchema


def validate_schema(request):
    try:
        text_extract = TextExtractSchema() \
            .load(request.get_json())
        return text_extract
    except:
        raise Exception("Invalid text extract schema")