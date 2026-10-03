import json


def orangecred(jpath):
 with open(jpath) as file:
    testdata = json.load(file)
    return testdata
