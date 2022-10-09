import re

NUMBER_PATTERN = re.compile(r'\d+(?:\.\d+|,\d+|\/\d+)?')


def get_numbers(sentences):
    numbers = []
    for sentence in sentences:
        if re.search(NUMBER_PATTERN, sentence):
            numbers.append(sentence)

    return numbers