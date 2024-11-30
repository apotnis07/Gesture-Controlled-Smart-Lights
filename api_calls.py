import json
from textwrap import indent

import requests



class API_Calls():

    def __init__(self, device="2D:4F:60:74:F4:8C:5B:22", model="H6006"):
    # smart_light_mac = "2D:4F:60:74:F4:8C:5B:22"
    # model = "H6006"
    # brightness1 = 20
        self.device = "2D:4F:60:74:F4:8C:5B:22"
        self.model = "H6006"
        with open('api_key.txt', 'r') as f:
            self.api_key = f.read()
        self.headers = {
        "Govee-API-Key" : self.api_key,
        "Content-Type" : "application/json"
        }

    def turn_on_light(self):
        with open('turn_on.json') as json_file:
            turn_on_body = json.load(json_file)
        turn_on_body['device'] = self.device
        turn_on_body['model'] = self.model

        url = "https://developer-api.govee.com/v1/devices/control"
        response = requests.put(url, headers=self.headers, json=turn_on_body)


        if response.status_code == 200:
            data = response.json()
            formatted_data = json.dumps(data, indent=2)
            print(formatted_data)
        else:
            print(f"Request failed with status code {response.status_code}")


    def turn_off_light(self):
        with open('turn_off.json') as json_file:
            turn_off_body = json.load(json_file)
        turn_off_body['device'] = self.device
        turn_off_body['model'] = self.model

        url = "https://developer-api.govee.com/v1/devices/control"
        response = requests.put(url, headers=self.headers, json=turn_off_body)


        if response.status_code == 200:
            data = response.json()
            formatted_data = json.dumps(data, indent=2)
            print(formatted_data)
        else:
            print(f"Request failed with status code {response.status_code}")

    def set_brightness(self, brightness = 100):
        with open('brightness.json') as json_file:
            brightness_body = json.load(json_file)
        brightness_body['device'] = self.device
        brightness_body['model'] = self.model
        brightness_body['cmd']['value'] = brightness

        url = "https://developer-api.govee.com/v1/devices/control"
        response = requests.put(url, headers=self.headers, json=brightness_body)


        if response.status_code == 200:
            data = response.json()
            formatted_data = json.dumps(data, indent=2)
            print(formatted_data)
        else:
            print(f"Request failed with status code {response.status_code}")

    # with open('api_key.txt', 'r') as f:
    #     api_key = f.read()

    # headers = {
    #     "Govee-API-Key" : api_key,
    #     "Content-Type" : "application/json"
    # }


    # with open('turn_off.json') as json_file:
    #     turn_off_body = json.load(json_file)
    #
    # with open('brightness.json') as json_file:
    #     brightness_body = json.load(json_file)
    #
    #
    #
    #
    # turn_off_body['device'] = smart_light_mac
    # turn_off_body['model'] = model
    #
    #
    # brightness_body['device'] = smart_light_mac
    # brightness_body['model'] = model
    # brightness_body['cmd']['value'] = brightness1
    #
    #
    # # url = "https://developer-api.govee.com/v1/devices/state?device=" + smart_light_mac + "&model=" + model
    # url = "https://developer-api.govee.com/v1/devices/control"
    # response = requests.put(url, headers=headers, json=brightness_body)




def main():
    calls = API_Calls()
    response = calls.turn_on_light()

    if response:
        if response.status_code == 200:
            data = response.json()
            formatted_data = json.dumps(data, indent=2)
            print(formatted_data)
        else:
            print(f"Request failed with status code {response.status_code}")

if __name__ == "__main__":
    main()