definition = {
        "type": "URL",
        "description": "Collects the webpage url",
        "score": 0,
        "score description": "The base score of the get_url getter is 0.",
        "notes": "Given that basic score is 0, the getter only serves to provide the webpage url."
        }


def get_url(source_url):
    return [definition, {'url': source_url, 'score': definition['score'], 'notes': ''}]