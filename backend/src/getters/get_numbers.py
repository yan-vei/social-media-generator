import re
from services import emoji_counter


definition = {
    'type': 'Numbers',
    'description': 'Get numbers from the data.',
    'score': 3,
    'score description': 'Block scores BestScore if it contains percents, money, big numbers(*llions, thousands). If block contains a fraction or a 2-digit number or bigger, it scores GoodScore. If block contains a date, year or a single digit - it gets BadScore score. The default should never occur.',
    'BestScore': 50,
    'GoodScore': 40,
    'MediumScore': 20,
    'BadScore': 10,
    'notes': 'Description of how the getter was scored',
    'generatedLength': 0
}

NUMBER_PATTERN = re.compile(r'\d+(?:\.\d+|,\d+|\/\d+)?')
DATE_PATTERN = re.compile(r'(\d{1,2})(\/|\.|\-)(\d{1,2})(\/|\.|\-)(\d{2,4})')


def is_invalid(sentence):
    return (re.search('[Cc]opyright', sentence) or re.search('©', sentence))


def is_year(number, sentence):
    in_year_pattern = r'(In|By|by|in|since|Since|it\'s|It\'s|for|For|after|After|From|from|To|to)\s(year\s)?' + str(number)
    return bool(re.search(in_year_pattern, sentence)) and len(number) == 4 and bool(re.search(r'[19\-20]\d+', number))


def is_date(number, sentence):
    # check months around that number
    months = [r'Jan(uary)?', r'Feb(uary)?', r'Mar(ch)?', r'Apr(il)?', r'May', 'Jun(e)?', r'Jul(y)?', r'Aug(ust)?',
              r'Sep(tember)?', r'Nov(emeber)?', 'Dec(ember)?']
    for month in months:
        month_match = re.search(month, sentence)
        if month_match:
            start = month_match.span()[0]
            end = month_match.span()[1]
            try:
                if re.search(number, sentence[start - 10:start]) or re.search(number, sentence[end:end + 10]):
                    return True
            except IndexError:  # if number is in the beginning/end of the sentence
                continue

    # if a number is a part of a date - it is a date
    dates = re.findall(DATE_PATTERN, sentence)
    if dates:
        for date in dates:
            for capture_group in date:
                if capture_group == number:
                    return True
    return False


def is_appended(number, sentence):
    appended_pattern = r'[a-zA-Z]{1,20}[\.,-;:\'\"]?' + str(number)
    return bool(re.search(appended_pattern, sentence))


def is_best(number, sentence):
    percent_pattern = r'(' + str(number) + r'\spercent)|(' + str(number) + '%)'
    big_pattern = str(number) + r'\s?(thousands?|\w{1,3}illions?|K)'
    money_pattern = r'(\$|€|£)' + str(number) + r'|' + str(number) + r'\s((dollar|euro|pound)s?)'
    return re.search(percent_pattern, sentence) or re.search(big_pattern, sentence) \
           or re.search(money_pattern, sentence)


def is_good(number, sentence):
    return (len(str(number)) >= 2 and not is_year(number, sentence) and not is_date(number, sentence)
            and not is_appended(number, sentence)) or '/' in str(number)

def is_medium(number):
    return len(str(number)) == 1


def is_bad(number, sentence):
    appended_pattern = r'[a-zA-Z]{1,20}[\.,-;:\'\"]?' + str(number)
    return is_year(number, sentence) or is_date(number, sentence) \
           or bool(re.search(appended_pattern, sentence))


def evaluate(number, sentence):
    score = definition["score"]
    if is_best(number, sentence):
        score = definition["BestScore"]
        note = '+' + str(definition["BestScore"]) +' many digits, percent, or money.'
    elif is_good(number, sentence):
        score = definition["GoodScore"]
        note = '+' + str(definition["GoodScore"]) +' 2 digits or more.'
    elif is_medium(number):
        score = definition["MediumScore"]
        note = '+' + str(definition["MediumScore"]) +' 1 digit'
    elif is_bad(number, sentence):
        score = definition["BadScore"]
        note = '+' + str(definition["BadScore"]) +' date.'
    return score, note


def get_numbers(sentences):
    result = [definition]

    for sentence in sentences:
        numbers = re.findall(NUMBER_PATTERN, sentence)
        if numbers:
            for number in numbers:
                if not is_invalid(sentence):
                    evaluation = evaluate(number, sentence)
                    emoji_count = emoji_counter.count_emoji(sentence)
                    result.append({
                        "result": sentence,
                        "score": evaluation[0],
                        "notes": evaluation[1],
                        "emoji_count": emoji_count
                    })

    result[0]["generatedLength"] = len(result) - 1

    return result