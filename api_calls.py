import json
from textwrap import indent

import requests

smart_light_mac = "2D:4F:60:74:F4:8C:5B:22"
model = "H6006"

with open('api_key.txt', 'r') as f:
    api_key = f.read()

headers = {
    "Govee-API-Key" : api_key,
    "Content-Type" : "application/json"
}

with open('turn_on.json') as json_file:
    turn_on_body = json.load(json_file)

with open('turn_off.json') as json_file:
    turn_off_body = json.load(json_file)

turn_on_body['device'] = smart_light_mac
turn_on_body['model'] = model


turn_off_body['device'] = smart_light_mac
turn_off_body['model'] = model

# url = "https://developer-api.govee.com/v1/devices/state?device=" + smart_light_mac + "&model=" + model
url = "https://developer-api.govee.com/v1/devices/control"
response = requests.put(url, headers=headers, json=turn_off_body)


if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=2)
    print(formatted_data)
else:
    print(f"Request failed with status code {response.status_code}")
