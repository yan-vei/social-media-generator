import json
from services import emoji_counter
import re
import os
from utils.check_env import SLASH

definition = {
    'type': 'Quotes',
    'description': 'Get anything in quotes and who said it from the data.',
    'score': 10,
    'ShortQuote': 0,
    'HasAuthor': 20,
    'AuthorInline': 30,
    'score description': 'Block gets +40 if the author is in the middle of the quote. Block gets +20 if quote has an author. Else - no upscoring. If the quote is less than 3 words - score is set to 0.',
    'notes': 'Description of how the getter was scored',
    'generatedLength': 0
}


QUOTES_PATTERN = [re.compile('("[A-Z0-9].+[.,?!]")'), re.compile("('[A-Z0-9].+[.,?!]')"), re.compile("(“[A-Z0-9].+[.,?!]”)")]
NAME_PATTERN = re.compile("[A-Z][a-z]{2,25} (?:[a-z]{0,4}\s{0,1}){0,2}[A-Z][a-z]{2,25}")
SHORT_NAME_PATTERN = re.compile("[A-Z][a-z]{2,25}")

dirname = os.getcwd()
filepath = os.path.join(dirname, 'data' + SLASH + 'verb-markers.json')
with open(filepath, 'r') as json_file:
    verb_markers = json.load(json_file)


def find_text_quotes(pattern, text):
    return re.findall(pattern, text)


def is_in_middle(quote):
    middle = None
    if re.search(r'”.+“', quote[1:-1]):
        middle = re.search(r'”.+“', quote[1:-1]).span(0)
    elif re.search(r'".+"', quote[1:-1]):
        middle = re.search(r'".+"', quote[1:-1]).span(0)

    if middle:
        for marker in verb_markers:
            if marker in quote[middle[0]:middle[1]] and re.search(SHORT_NAME_PATTERN, quote[middle[0]:middle[1]]):
                return True
    return False


def searchPart(part):
    for marker in verb_markers:
        if marker in part:
            author = re.search(NAME_PATTERN, part)
            if author:
                return author.group(0)

    return ''


def find_source(quote, paragraph):
    start = paragraph.find(quote)
    end = start + len(quote)
    counterLeft = start
    counterRight = end
    leftPart, rightPart = '', ''

    if start != -1: # if quote in the paragraph fully:
        while counterLeft > 0:
            if paragraph[counterLeft] in """.?!""" and paragraph[counterLeft + 1] == ' ' and re.match(r'[A-Z]', paragraph[counterLeft + 2]):
                leftPart = paragraph[counterLeft + 2:start]
                break
            elif paragraph[counterLeft] in """.?!""" and paragraph[counterLeft + 1] == ' ' and re.match(r'[a-z]', paragraph[counterLeft - 1]):
                break
            counterLeft -= 1

        authorLeft = searchPart(leftPart)
        if authorLeft != '':
            return authorLeft

        if end < len(paragraph) and not re.match(r'\.', paragraph[end-1]):
            while counterRight < len(paragraph):
                if paragraph[counterRight] in """.?!""" and re.match(r'[a-z]', paragraph[counterRight - 1]):
                    rightPart = paragraph[end:counterRight]
                    break
                counterRight += 1

        authorRight = searchPart(rightPart)
        if authorRight != '':
            return authorRight

    return ''


def evaluate(quote, author, middle):
    score = definition['score']
    words = quote.split(' ')

    if len(words) < 3:
        return (definition["ShortQuote"], str(definition["ShortQuote"])+' too short quote. ')
    elif middle:
        return (score+definition["AuthorInline"], str(definition["AuthorInline"])+' author inside quote. ')
    elif author != '':
        return (score+definition["HasAuthor"], str(definition["HasAuthor"])+' quote with author. ')

    return score, ''


def form_quote_result(quote, author, middle):
    evaluation = evaluate(quote, author, middle)
    emoji_count = emoji_counter.count_emoji(quote)
    if author != '':
        return {'result': str(quote) + ' ' + str(author), 'quote': str(quote), 'author': str(author),
                'score': evaluation[0], 'notes': evaluation[1], 'emoji_count': emoji_count}
    else:
        return {'result': str(quote), 'quote': quote, 'score': evaluation[0], 'notes': evaluation[1],
                'emoji_count': emoji_count}


def get_quotes(paragraphs):
    result = [definition]

    for paragraph in paragraphs:
        paragraph = paragraph.get_text(' ')

        for pattern in QUOTES_PATTERN:
            quotes = find_text_quotes(pattern, paragraph)

            if quotes:
                for quote in quotes:
                    authorInMiddle = is_in_middle(quote)
                    quote_author = ''

                    if not authorInMiddle:
                        quote_author = find_source(quote, paragraph)

                    result.append(form_quote_result(quote, quote_author, authorInMiddle))

    result[0]["generatedLength"] = len(result) - 1

    return result