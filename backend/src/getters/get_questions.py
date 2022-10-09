import re

QUESTION_PATTERN = re.compile(r'[A-Z][\w\’;:,\'\s]*\?')


def get_questions(text):
    questions = re.findall(r'[A-Z][\w\’;:,\'\s]*\?', text)
    return questions