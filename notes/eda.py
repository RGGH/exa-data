from pprint import pprint
import json

test_file = "data/Zane918_Schoen8_4995ca99-2ab9-3b18-a56e-c33d29e53af0.json"

# load one file
with open(test_file) as json_file:
    data_dict = json.load(json_file)


def flatten(current, key, result):
    if isinstance(current, dict):
        for k in current:
            new_key = "{0}.{1}".format(key, k) if len(key) > 0 else k
            flatten(current[k], new_key, result)
    else:
        result[key] = current
    return result

result = flatten(data_dict, '', {})

pprint (result)
