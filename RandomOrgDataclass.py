'''
contains the api information for random.org
more information can be found here:
https://api.random.org/json-rpc/4/basic
'''

class RandomOrgAPIs:
    def __init__(self):
        '''initializes the api dictionary'''
        self.api_dict: dict
        self.api_key: str
    
    def set_api_key(self, api_key: str):
        '''sets the api key'''
        self.api_key = api_key
        self._initialize_api_dict()

    def get_api_dict(self) -> dict:
        '''returns the api dictionary'''
        return self.api_dict
    
    def get_single_api(self, api_name: str) -> dict:
        '''the api_name conforms to the methods found on the random.org website'''
        return self.api_dict[api_name]
    
    def _initialize_api_dict(self):
        self.api_dict = {
            "generateIntegerSequences": {
                "jsonrpc": "2.0",
                "method": "generateIntegerSequences",
                "params": {
                    "apiKey": self.api_key,
                    "n": 3,
                    "length": 10,
                    "min": 1,
                    "max": 6,
                    "replacement": True,
                    "base": 10
                },
                "id": 1
            },
            "generateIntegers": {
                "jsonrpc": "2.0",
                "method": "generateIntegers",
                "params": {
                    "apiKey": self.api_key,
                    "n": 6,
                    "min": 1,
                    "max": 6,
                    "replacement": True
                },
                "id": 1
            },
            "generateStrings": {
                "jsonrpc": "2.0",
                "method": "generateStrings",
                "params": {
                    "apiKey": self.api_key,
                    "n": 3,
                    "length": 10,
                    "characters": "abcdefghijklmnopqrstuvwxyz",
                    "replacement": True
                },
                "id": 1
            },
            "generateDecimalFractions": {
                "jsonrpc": "2.0",
                "method": "generateDecimalFractions",
                "params": {
                    "apiKey": self.api_key,
                    "n": 3,
                    "decimalPlaces": 2,
                    "replacement": True
                },
                "id": 1
            },
            "generateGaussians": {
                "jsonrpc": "2.0",
                "method": "generateGaussians",
                "params": {
                    "apiKey": self.api_key,
                    "n": 3,
                    "mean": 0,
                    "standardDeviation": 1,
                    "significantDigits": 5
                },
                "id": 1
            },
            "generateBlobs":{
                "jsonrpc": "2.0",
                "method": "generateBlobs",
                "params": {
                    "apiKey": self.api_key,
                    "n": 3,
                    "size": 1024,
                    "format": "hex"
                },
                "id": 1
            },
            "generateUUIDs": {
                "jsonrpc": "2.0",
                "method": "generateUUIDs",
                "params": {
                    "apiKey": self.api_key,
                    "n": 3
                },
                "id": 1
            }
        }