import json

import requests


URL = "http://127.0.0.1:8000/empapi -H 'Authorization: Token ab30ed8e4e5c042ce19c7159702d628edd93eaf1461021946d4731760faec58c'"

def get_data():
    headers = {"content-Type":"application/json",
    }
    r = requests.get(url=URL, headers=headers)
    data = r.json()
    print(data)

    
# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {"id":id}
#     json_data = json.dumps(data)
#     headers = {"content-Type":"application/json",
#     "token": "ab30ed8e4e5c042ce19c7159702d628edd93eaf1461021946d4731760faec58c"
#     }
#     r = requests.get(url=URL, headers=headers, data=json_data)
#     data = r.json()
#     print(data)

get_data()