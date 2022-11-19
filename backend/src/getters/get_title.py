from backend.src.services import emoji_counter

definition = {
        "type": "Title",
        "description": "Get title of the article.",
        "score": 30,
        "notes": "Description of how the getter was scored",
        'generatedLength': 0
        }


def find_title(soup):
    header = soup.find('h1')
    if header is not None:
        return header.get_text(' ')
    else:
        return ''


def is_not_duplicated(title, firstSentences):
    firstSentences.pop(0)
    for sentence in firstSentences:
        if sentence['result'] == title or sentence['result'] in title or title in sentence['result']:
            return False
    return True


def evaluate():
    score = definition['score']
    note = ''
    return score, note


def get_excerpt_title(excerpt_title):
    result = [definition]
    title = {}
    title['result'] = excerpt_title

    title['emoji_count'] = emoji_counter.count_emoji(title['result'])
    score, note = evaluate()
    title['score'] = score
    title['notes'] = note
    result.append(title)

    result[0]["generatedLength"] = len(result) - 1

    return result


def get_title(soup, firstSentences):
    result = [definition]

    title = {}
    title['result'] = find_title(soup)

    if title['result'] != '' and is_not_duplicated(title['result'], firstSentences):
        title['emoji_count'] = emoji_counter.count_emoji(title['result'])
        score, note = evaluate()
        title['score'] = score
        title['notes'] = note
    result.append(title)

    result[0]["generatedLength"] = len(result) - 1

    return result