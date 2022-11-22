import json


definition = {
    'type': 'AlwaysValidCTAs',
    'description': 'Supply all the always valid CTAs for the templateEngine along with topics, emojies, hashtags, etc.',
    'score': 'spreadsheet_score',
    'score description': 'Score is assigned to each always valid call to action based on the score from the spreadsheet',
    'notes': 'Description of how the getter was scored',
    'generatedLength': 0
}


jsonfile = open('data/calls-to-actions.json')
calls_to_action = json.load(jsonfile)


def get_calls_to_action():
    result = [definition]

    for call in calls_to_action:
        call_to_action = {}

        call_to_action['result'] = call['call']
        call_to_action['score'] = int(call['score'])
        call_to_action['notes'] = "Score for the CTA was set to " + str(call['score'])
        call_to_action['emoji_count'] = call['emoji_count']

        result.append(call_to_action)

    result[0]["generatedLength"] = len(result) - 1

    return result