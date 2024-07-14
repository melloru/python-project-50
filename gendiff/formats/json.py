import json


def to_format(diff):
    return json.dumps(diff, indent=2)
