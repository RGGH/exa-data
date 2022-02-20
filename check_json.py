
import json
from pprint import pprint
from typing import Dict, List

# Opening JSON file
f = open('data/Abbey813_Price929_83524678-9bff-93b7-ef89-d7f5390072ff.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
entry = (data['entry'])
#pprint(entry[1])

def entry_full_url():
    ls = []
    for fullUrl in entry:
        ls.append(fullUrl)
    return ls


cleaned_list = entry_full_url()
for full in cleaned_list:

    ''' Handle TypeError: 'NoneType' object is not subscriptable '''
    try:

        extension = full.get('resource').get('extension')[0]
        print(extension)
        if extension == None: 
            print("None Type - Dictionary missing")

        if isinstance(extension, Dict):
            extension = extension.get('url')
            print(type(extension))
        else:
            if isinstance(extension, List):
                extension = full.get('resource').get('extension')[0].get('url')
                print(extension)
    except TypeError as te:
        print(te)



