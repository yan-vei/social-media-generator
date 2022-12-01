import re
import json

from tweet_shortner import *
import os

from utils.check_env import SLASH

definition = {
        "type": "templateEngine",
        "description": "Recursively generate tweets for all templates and all data",
        "score": "template_score",
        "score description": "The scoring is first calculated to be an average of the getters used to create the tweet. "+
            "The engine supports down or upscaling getter blocks that match the character limit in the template"+
            "The entire tweet is then scored based on the length, counting a URL as defined in 'TweetURLLength.'"+
            "If the length is more than the max 'TweetLength', it downscores with 'Penalty Long Tweet'.  "+
            "If the length is even worse, and more than 'Tweet Fail Length', it downscores with 'Penalty Fail Length'.  "+
            "Because we favor full tweets, if the tweet is not too long and more than 'Tweet Golden Length', we add 'Upscore Golden Length'.",
        'Tweet Fail Length': 320,
        'Penalty Fail Length': 30,
        'TweetLength': 280,
        'TweetURLLength': 23 +1,
        'TweetLength Scores': {'291-300': 2, '281-290': 4, '270-280': 10, '260-269': 7,
                               '250-259': 4, '240-249': 2, '230-239': 1},
        "generatedLength": "length of what we are returning"
        }


global templates
dirname = os.getcwd()
filepath = os.path.join(dirname, 'data' + SLASH + 'templates.json')
jsonFile = open(filepath, encoding='utf-8')
templates = json.load(jsonFile)
jsonFile.close()
tweetbook = [definition]


def generate_tweets(text, template, score, depth, notes, lengthoffset, block_emojies):
    depth += 1
    tags = re.findall(r'\[(.*?)\]' ,text)
    firsttag = tags[0]

    if ":" not in firsttag:
        firsttag += ":result"
    getter = firsttag.split(":", 1)[0]
    if getter not in result:
        return "invalid getter"
    dataset = result[getter].copy()
    dataset.pop(0)

    for block in dataset:
        gettertags = re.findall(r'\[('+getter+'.*?)\]' ,text)
        tweet = text
        newnote = notes
        blockscore = score

        for tag in gettertags:
            safetag = tag
            if ":" not in safetag:
                safetag += ":result"
            if "%" not in safetag:
                safetag += "%0"
            itemdata, lengthlimit = safetag.split("%", 1)
            lengthlimit = int(lengthlimit)
            detail = itemdata.split(":", 1)[1]

            if detail not in block:
                continue

            tagdata = block[detail]
            if lengthlimit > 0:
                if len(tagdata) > lengthlimit:
                    tagdata = send_to_shorten(tagdata, lengthlimit)

            if getter == 'URL' and detail == 'url':
                lengthoffset += len(tagdata) - int(definition["TweetURLLength"])

            tweet = re.sub(r'\['+tag+'\]', tagdata, tweet, count=1)

        if "emoji_count" in block:
            block_emojies += block['emoji_count']

        if "score" in block:
            blockscore += block['score']

            if getter == "URL" and depth > 1:
                depth -= 1

            newnote += " " + getter
            if block['notes'] != '':
                newnote += " (" + block['notes']+ ")"
            newnote += ": +" + str(block['score']) + " (" + str(blockscore) + "/" + str(depth) + "=" + str(float(blockscore / depth)) + ") "

        if len(re.findall(r'\[('+getter+'.*?)\]', tweet)) > 0:
            continue


        if len(re.findall(r'\[(.*?)\]' ,tweet)) > 0:
            generate_tweets(tweet, template, blockscore, depth, newnote, lengthoffset, block_emojies)
        else:
            tweetLength = (int(len(tweet) - lengthoffset)) + template_emoji + block_emojies
            finalscore = float(blockscore / depth) + template_score

            # Tweet shortening
            if tweetLength > int(definition['TweetLength']):
                tweet = send_to_shorten(tweet, definition['TweetLength'], lengthoffset)
                tweetLength = (int(len(tweet) - lengthoffset)) + template_emoji + block_emojies # check again after shortening

            if tweetLength > int(definition['Tweet Fail Length']):
                finalscore -= float(definition['Penalty Fail Length'])
                newnote += "Fail Length Tweet: -" + str(definition['Penalty Fail Length']) + " "
            else:
                for lengthRange in definition['TweetLength Scores']:
                    if int(lengthRange[:3]) <= tweetLength <= (int(lengthRange[4:7])):
                        finalscore += int(definition['TweetLength Scores'][lengthRange])
                        newnote += "TweetLength (" + str(lengthRange) + "): +" + str(definition['TweetLength Scores'][lengthRange]) + ". "
                        break

            tweetbook.append({
                "post": tweet,
                "template": template,
                "score": finalscore,
                "notes": newnote,
                "length": tweetLength,
                })
    return None


def get_tweets(data):
    global tweetbook, template_score, template_emoji, result
    result = data
    tweetbook = [definition]

    for template in templates:
        line = template['result']
        template_score = template['score']
        template_emoji = template['emoji_count']
        note = 'Template score: +' + str(template['score']) + '.'

        generate_tweets(line, line, 0, 0, note, 0, 0)
    tweetbook[0]["generatedLength"] = len(tweetbook) -1
    return tweetbook