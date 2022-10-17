import re
from backend.src.services import emoji_counter

definition = {
    'type': 'FirstSentence',
    'description': 'Get every first sentence of each paragraph.',
    'FirstSentScore': 30,
    'SecondSentScore': 25,
    'ThirdSentScore': 20,
    'OtherSentScore': 15,
    'score description': 'Scoring taking position downscore into account. Base score 30 for the first one, 25, 20, 15 for the last section.',
    'notes': 'Description of how the getter was scored',
    'generatedLength': 0
}


SENTENCE_PATTERN = re.compile(r"[A-Z][^\.!?]*[\.!?]")
QUOTATION_MARKS = """"'“”"""


def evaluate_exceptions(sentence):
    endOfSentence = sentence[len(sentence)-3:len(sentence)-1]

    if re.search(r'[A-Z]', endOfSentence):
        return ''

    return sentence


def extract_quote(paragraphText):
    quotation_marks = """"“”"""
    quote_opened = False

    charIndex = 0
    while charIndex < len(paragraphText):
        if paragraphText[charIndex] in "?.!" and quote_opened == False:
            break
        elif paragraphText[charIndex] in quotation_marks and quote_opened == False and (re.match(r' ', paragraphText[
            charIndex - 1]) or charIndex == 0):
            if charIndex+1 < len(paragraphText) and re.match(r'[A-Z]', paragraphText[charIndex+1]):
                quote_opened = True
        elif paragraphText[charIndex] in quotation_marks and quote_opened == True and re.match(r'[.?!]', paragraphText[
            charIndex - 1]):
            return paragraphText[:charIndex+1]
        charIndex += 1

    return ''


def getFirstSent(paragraph):
    if type(paragraph) != str:
        paragraphText = paragraph.get_text(' ')
    else:
        paragraphText = paragraph
    firstQuote = extract_quote(paragraphText)

    if firstQuote == '':
        sentence = re.search(SENTENCE_PATTERN, paragraphText)
        if sentence:
            return sentence.group()
        else:
            return paragraphText

    return firstQuote


def evaluate(par_counter):
    if par_counter == 1:
        score = definition['FirstSentScore']
    elif par_counter == 2:
        score = definition['SecondSentScore']
    elif par_counter == 3:
        score = definition['ThirdSentScore']
    else:
        score = definition['OtherSentScore']

    note = '+' + str(score) + ' P' + str(par_counter) + '.'

    return score, note


def get_first_sentence(paragraphs):
    result = [definition]

    par_counter = 0
    for paragraph in paragraphs:
        par_counter += 1

        sentence = getFirstSent(paragraph)
        if evaluate_exceptions(sentence) == '':
            continue

        evaluation = evaluate(par_counter)
        emoji_count = emoji_counter.count_emoji(sentence)

        result.append(
            {'result': sentence,
             'score': evaluation[0],
             'notes': evaluation[1],
             'emoji_count': emoji_count
             })

    result[0]["generatedLength"] = len(result) -1


    return result

