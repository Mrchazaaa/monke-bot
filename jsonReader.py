import json

def getValue(key):
    global jsonStore

    try:
        return jsonStore[key]
    except NameError:
        with open('.config.json', 'r') as f:
            jsonStore = json.load(f)
        return jsonStore[key]

