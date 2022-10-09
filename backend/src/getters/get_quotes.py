import re

QUOTES_PATTERN = [re.compile('("[A-Z0-9].+[.,?!]")'), re.compile("('[A-Z0-9].+[.,?!]')"), re.compile("(“[A-Z0-9].+[.,?!]”)")]
NAME_PATTERN = re.compile("[A-Z][a-z]{2,25} (?:[a-z]{0,4}\s{0,1}){0,2}[A-Z][a-z]{2,25}")
SHORT_NAME_PATTERN = re.compile("[A-Z][a-z]{2,25}")


def has_quotes(pattern, text):
    return re.search(pattern, text)


def get_quotes(sentences):
    quotes = []
    for pattern in QUOTES_PATTERN:
        for sentence in sentences:
            if has_quotes(pattern, sentence):
                quotes.append(sentence)

    return quotes
