'''calls an API to get random numbers'''
# sources:
# https://api.random.org/json-rpc/4/basic

import requests
import json
from abc import ABC, abstractmethod

class RandomOrg(ABC):
    def __init__(self):
        self.response_data: list
        self.api_key: str = "407922a8-beb5-4184-9da4-0549cd2a0a90"
    
    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_random_data(self):
        pass

    @abstractmethod
    def set_random_frame(self, values: dict):
        pass


class RandomValues(RandomOrg):
    def __init__(self):
        super().__init__()
        '''
        gets a range of integers
        self.min and self.max are both inclusive
        self.method: str = defines the possible methods
        '''
        self.amount: int
        self.min: int
        self.max: int
        self.response: str = ""
        self.response_data: list
        self.replacement: bool = True
        self.method: str = "generateIntegers"
    
    def set_random_frame(self, values: dict):
        '''
        sets the values for the random integers:
        example:
        values = {'amount': int, 'min': int, 'max': int, replacement: True|False}
        '''
        self.amount = values["amount"]
        self.min = values["min"]
        self.max = values["max"]
        self.replacement = values["replacement"]
    
    def set_method(self, method: str):
        '''
        sets the method to get the random numbers
        method = 
            generateIntegers
            generateIntegerSequences
            generateDecimalFractions
            generateGaussians
            generateStrings
            generateUUIDs
            generateBlobs
        '''
        self.method = method
    
    def get_random_data(self) -> list:
        '''returns a list of integers'''
        return self.response_data["result"]["random"]["data"]
    
    def connect_to_api(self):
        '''creates a request to random.orgs API'''
        # https://www.random.org/sequences/?min=1&max=52&col=1&format=plain&rnd=new
        raw_data = {
            "jsonrpc": "2.0",
            "method": self.method,
            "params": {
                "apiKey": self.api_key,
                "n": self.amount,
                "min": self.min,
                "max": self.max,
                "replacement": self.replacement
            },
            'id':1
        }

        headers = {'Content-type': 'application/json','Content-Length': '200', 'Accept': 'application/json'}
        data=json.dumps(raw_data)
        self.response = requests.post(
            url='https://api.random.org/json-rpc/2/invoke',
            data=data,
            headers=headers
            )
        self.response_data = json.loads(self.response.content)

if __name__ == "__main__":
    zufall = RandomValues()
    zufall.set_method("generateIntegers")
    zufall.set_random_frame({"amount": 10, "min": 1, "max": 100, "replacement": True})
    zufall.connect_to_api()
    print(zufall.get_random_data())
