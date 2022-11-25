import json
import re
import os


global shortenings
dirname = os.getcwd()
filepath = os.path.join(dirname, 'data\\shortenings.json')
jsonFile = open(filepath, encoding='utf-8')
shortenings = json.load(jsonFile)
jsonFile.close()


def convert_reg_nums(text, exceptions):
    tokens = text.split(' ')
    starting_nos = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                    "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    higher_nos = ["hundred", "thousand"]

    starting_nos_dict = dict()
    for i in range(len(starting_nos)):
        starting_nos_dict[starting_nos[i]] = i

    tens_dict = dict()
    for i in range(len(tens)):
        tens_dict[tens[i]] = (i + 2) * 10

    higher_nos_dict = {"hundred": 100, "thousand": 1000}

    # cleanup of exceptions:
    for exception in exceptions:
        if exception in starting_nos:
            starting_nos.remove(exception)
            starting_nos_dict.pop(str(exception))
        elif exception in tens:
            tens.remove(exception)
            tens_dict.pop(str(exception))

    temp_number = 0
    final_number = 0

    point_flag = False
    less_ten_flag = False
    number_flag = False

    final_string = ""

    tokens.append("")


    for i in range(len(tokens)):

        word = tokens[i]

        if (word.lower() in starting_nos or word.lower() in tens or word.lower() in higher_nos) and point_flag == False:

            number_flag = True

            if word.lower() in starting_nos:
                temp_number = temp_number + starting_nos_dict[word.lower()]
            elif word.lower() in tens:
                temp_number = temp_number + tens_dict[word.lower()]

            elif word.lower() == "hundred":
                temp_number = temp_number * 100

            elif word.lower() == "thousand":
                final_number = final_number + temp_number * higher_nos_dict[word.lower()]
                temp_number = 0

        elif word.lower() in starting_nos and point_flag == True:
            final_string += str(starting_nos_dict[word.lower()])


        elif (word == "and" and (
                tokens[i + 1] in starting_nos or tokens[i + 1] in tens or tokens[i + 1] in higher_nos)):
            continue

        elif (word.lower() == "point" and (
                tokens[i + 1] in starting_nos or tokens[i + 1] in tens or tokens[i + 1] in higher_nos)):

            final_number = final_number + temp_number

            point_flag = True
            number_flag = False
            final_string += " " + str(final_number) + "."
            continue

        else:
            point_flag = False

            if number_flag == True:

                final_number = final_number + temp_number

                if int(final_number) < 10:
                    less_ten_flag = True
                    break

                if word != "." and word != "?" and word != "!":
                    final_string += " " + str(final_number) + " " + word
                else:
                    final_string += " " + str(final_number) + word
                number_flag = False
            else:
                if word != "." and word != "?" and word != "!":
                    final_string += " " + word
                else:
                    final_string += word
            final_number = 0
            temp_number = 0

    if less_ten_flag:
        return text

    final_string = final_string[1:-1]
    return final_string


def convert_hyphen_nums(text):
    regs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    regs_dict = dict()
    for i in range(len(regs)):
        regs_dict[regs[i]] = i+1

    tens_dict=dict()
    for i in range(len(tens)):
        tens_dict[tens[i]]=(i+2)*10

    tokens = text.split()
    hyphen_num = re.compile(r'\w+\-\w+')

    found_nums = []

    for token in tokens:
        if re.search(hyphen_num, token):
            numbers = token.split('-')
            number = None
            if numbers[0] in tens_dict and numbers[1] in regs_dict:
                number = tens_dict[numbers[0]] + regs_dict[numbers[1]]
            elif numbers[0] in regs_dict and numbers[1] in regs_dict:
                number = regs_dict[numbers[0]] + regs_dict[numbers[1]]
            elif numbers[0] in regs_dict and numbers[1] in tens_dict:
                number = regs_dict[numbers[0]] + tens_dict[numbers[1]]
            if number:
                found_nums.append({'word': token, 'number': number})

    for number in found_nums:
        text = text.replace(number['word'], str(number['number']))

    return text


def replace_symbol(tweet, sub, symbol):
    sub = ' ' + str(sub) + ' ' # replace what
    symbol = ' ' + str(symbol) # replace with

    return tweet.replace(sub, symbol)


def get_exceptions(tweet):
    exceptions = []
    resultExceptions = []

    for exception in exceptions:
        if tweet.find(exception['rule']) != -1:
            resultExceptions.append(exception['exception'])

    return resultExceptions


def shorten(tweetPiece, aggressiveness):
    exceptions = get_exceptions(tweetPiece)
    if aggressiveness == 1:
        tweetPiece = convert_reg_nums(tweetPiece, exceptions)
        tweetPiece = convert_hyphen_nums(tweetPiece)

    for shortening in shortenings:
        if shortening['aggressiveness'] == aggressiveness and shortening['item'].strip() not in exceptions:
            tweetPiece = replace_symbol(tweetPiece, shortening['item'], shortening['replacement'])

    return tweetPiece


def getTweetLength(tweetPiece, lengthOffset):
    if lengthOffset:
        return int(len(tweetPiece) - lengthOffset)
    else:
        return int(len(tweetPiece))


def send_to_shorten(tweetPiece, limitLength, lengthOffset=None):
    global shortenings
    aggressiveness = 1

    tweetLength = getTweetLength(tweetPiece, lengthOffset)

    while tweetLength > limitLength and aggressiveness < 3:
        tweetPiece = shorten(tweetPiece, aggressiveness)
        tweetLength = getTweetLength(tweetPiece, lengthOffset)
        aggressiveness += 1

    return tweetPiece