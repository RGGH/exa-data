
import json
from pprint import pprint
from typing import Dict

# Opening JSON file
f = open('/home/rag/env/exa-data-1/exa-data/data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json')

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
    # #print(full)
    full_url = full.get('fullUrl')
    print(full_url)
    # resource = full.get('resource')
    # # print(resource)
    # # print("\n\n\n")
    # #print(resource)

    # # resource_resource_type = full.get('resource').get('resourceType')
    # # print(resource_resource_type)
    # # # #
    # # # #
    # # #

    # # div_ = resource.get('text','0')
    # # if isinstance(div_, Dict):
    # #     div_ = div_.get('div')
    # #     print(div_)
    # # else:
    # #     print("no value")

    # ex = resource.get('url','0')

    # if isinstance(ex, Dict):
    #     ex = ex.get('url')
    #     print(ex)
    # else:
    #     print("no ex")       



# #    # extension
#     coding = full.get('resource').get('category')#[0].get('coding')[0]
#     if isinstance(coding,Dict):
#         coding = coding.get('coding')
#         print(coding)
#     else:
#         print("no coding")


