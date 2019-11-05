import json
import os.path

def getValue(key):
    global jsonStore

    try:
        return jsonStore[key]
    except NameError:
        with open('.config.json', 'r') as f:
            jsonStore = json.load(f)
        return jsonStore[key]
        
# global inProduction
# if os.path.exists('./config.json'):
#     inProduction = False
# else:
#     inProduction = True