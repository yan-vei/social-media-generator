definition = {
        "type": "Source",
        "description": "Get source of the article.",
        "score": 0,
        "notes": "Description of how the getter was scored",
        'generatedLength': 0
        }


def get_source(source):
    result = [definition]

    result.append(
        {
            'source': source,
            'score': definition['score'],
            'notes': ''
        }
    )
    result[0]["generatedLength"] = len(result) - 1

    return result