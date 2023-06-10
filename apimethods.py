'''
ApiMethods class handles the construction of the json-rpc request
ApiRequest class handles the request to the api and returns the response
these classes are used in randommethods.py, which is the main file
'''

# Copyright:
# (c) 2023, Torsten Drever (https://github.com/Brakau-TD)
# apimethods.py is part of randommethods.py
# see the MIT license in randommethods.py
# these two files are needed to work together
# you will also need an api_key.py file with your API key in a variable: 
# api_key = "<your api key>"
# you can register for an API key here:
# https://accounts.random.org/


import requests
import json
from api_key import api_key

class ApiMethods:
    '''handles construction of the json-rpc request'''
    def __init__(self):
        self.api_dict: dict
        self.api_key: str = api_key

    def construct_api_dict(self,method: str) -> str|bool:
        '''
        creates an api dictionary for the given method
        method names are:
        - IntegerSequences
        - Integers
        - Strings
        - DecimalFractions
        - Gaussians
        - Strings
        - UUIDs
        - Blobs
        they are case sensitive and get prefixed with "generate"
        '''
        if method.upper() not in ["INTEGERSEQUENCES","INTEGERS","STRINGS","DECIMALFRACTIONS","GAUSSIANS","UUIDS","BLOBS","USAGE"]:
            print("Error: method not found")
            return False
        elif method.upper() == "USAGE":
            method_name = "getUsage"
        else:
            method_name = "generate" + method if method[0].isupper() else "generate" + method.capitalize()
        self.api_dict = {
                "jsonrpc": "2.0",
                "method": method_name,
                "params": {
                    "apiKey": self.api_key
                },
                "id": 1
            }
        return method_name
    
    def complete_api_dict(self, method_name: str, values: dict|None = None) -> dict|bool:
        request = getattr(self, method_name)(values)
        if request:
            self.api_dict = request
        else:
            print("Error: request not created")
            return False
        return self.api_dict
 
    def generateIntegerSequences(self, values: dict) -> dict|bool:
        try:
            self.api_dict["params"]["n"] = values["n"]
            self.api_dict["params"]["length"] = values["length"]
            self.api_dict["params"]["min"] = values["min"]
            self.api_dict["params"]["max"] = values["max"]
            self.api_dict["params"]["replacement"] = values["replacement"]
            self.api_dict["params"]["base"] = values["base"]
        except KeyError as e:
            print(f'KeyError: {e}')
            return False
        return self.api_dict

    def generateIntegers(self, values: dict) -> dict|bool:
        try:
            self.api_dict["params"]["n"] = values["n"]
            self.api_dict["params"]["min"] = values["min"]
            self.api_dict["params"]["max"] = values["max"]
            self.api_dict["params"]["replacement"] = values["replacement"]
            self.api_dict["params"]["base"] = values["base"]
        except KeyError as e:
            print("KeyError: ",e)
            return False
        return self.api_dict

    def generateStrings(self, values: dict) -> dict|bool:
        try:
            self.api_dict["params"]["n"] = values["n"]
            self.api_dict["params"]["length"] = values["length"]
            self.api_dict["params"]["characters"] = values["characters"]
            self.api_dict["params"]["replacement"] = values["replacement"]
        except KeyError as e:
            print(f'KeyError: {e}')
            return False
        return self.api_dict

    def generateDecimalFractions(self, values: dict) -> dict|bool:
        try:
            self.api_dict["params"]["n"] = values["n"]
            self.api_dict["params"]["decimalPlaces"] = values["decimalPlaces"]
            self.api_dict["params"]["replacement"] = values["replacement"]
        except KeyError as e:
            print(f'KeyError: {e}')
            return False
        return self.api_dict

    def generateGaussians(self, values: dict) -> dict|bool:
        try:
            self.api_dict["params"]["n"] = values["n"]
            self.api_dict["params"]["mean"] = values["mean"]
            self.api_dict["params"]["standardDeviation"] = values["standardDeviation"]
            self.api_dict["params"]["significantDigits"] = values["significantDigits"]
        except KeyError as e:
            print(f'KeyError: {e}')
            return False
        return self.api_dict

    def generateUUIDs(self, values: dict) -> dict|bool:
        try:
            self.api_dict["params"]["n"] = values["n"]
        except KeyError as e:
            print(f'KeyError: {e}')
            return False
        return self.api_dict

    def generateBlobs(self, values: dict) -> dict|bool:
        if not 0 < values["size"] < 1048576:
            print("Error: size must be between 1 and 1048576")
            return False
        if not values["format"] in ["base64", "hex"]:
            print("Error: format must be base64 or hex")
            return False
        if not values["n"] in range(1,101):
            print("Error: n must be between 1 and 100")
            return False
        try:
            self.api_dict["params"]["n"] = values["n"]
            self.api_dict["params"]["size"] = values["size"]
            self.api_dict["params"]["format"] = values["format"]
        except KeyError as e:
            print(f'KeyError: {e}')
            return False
        return self.api_dict
    
    def getUsage(self, *args) -> dict:
        self.api_dict = {
                "jsonrpc": "2.0",
                "method": "getUsage",
                "params": {
                    "apiKey": self.api_key
                },
                "id": 1258
            }
        return self.api_dict

    
class ApiRequest:
    '''handles the request to random.orgs API'''
    def __init__(self):
        '''
        initializes the response and response_data
        attributes are only used internally
        and are created when the connect_to_api method is called
        '''
        self._response: requests.Response
        self._response_data: dict

    def connect_to_api(self, api_dict) -> dict:
        '''
        creates a request to random.orgs API
        https://www.random.org/sequences/?min=1&max=52&col=1&format=plain&rnd=new
        '''
        headers = {'Content-type': 'application/json','Content-Length': '200', 'Accept': 'application/json'}
        data=json.dumps(api_dict)
        self._response = requests.post(
            url='https://api.random.org/json-rpc/2/invoke',
            data=data,
            headers=headers
            )
        self._response_data = json.loads(self._response.content)
        return self._response_data
    