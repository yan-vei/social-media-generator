import json


jsonfile = open('data/calls_to_actions.json')
calls_to_action = json.load(jsonfile)


def get_calls_to_action():
    calls_to_action = []

    for call in calls_to_action:
        call_to_action = {}

        call_to_action['result'] = call['call']
        call_to_action['score'] = int(call['score'])

        calls_to_action.append(call_to_action)

    return calls_to_action