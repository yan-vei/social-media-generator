import re
from backend.src.services import emoji_counter


definition = {
    'type': 'Question',
    'description': 'Get questions from the data.',
    'GoodScore': 50,
    'BadScore': 10,
    'score description': 'Block scores GoodScore if it contains 3 or more words. Block scores BadScore if it has less than 3 words.',
    'notes': "Description of how the getter was scored",
    'generatedLength': 0
}


QUESTION_PATTERN = re.compile(r'[A-Z][\w\’;:,\'\s]*\?')


def evaluate(question):
    words = question.split(' ')
    if len(words) >= 3:
        score = definition['GoodScore']
        note = '+' + str(definition["GoodScore"]) + ' 3 words or more.'
    else:
        score = definition['BadScore']
        note = '+' + str(definition["BadScore"]) + ' Less than 3 words.'

    return score, note


def get_questions(text):
    result = [definition]
    questions = re.findall(QUESTION_PATTERN, text)

    if questions:
        for question in questions:
            evaluation = evaluate(question)
            emoji_count = emoji_counter.count_emoji(question)
            result.append({
                "result": question,
                "score": evaluation[0],
                "notes": evaluation[1],
                "emoji_count": emoji_count
            })

    result[0]["generatedLength"] = len(result) - 1

    return result
