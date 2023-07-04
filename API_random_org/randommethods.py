'''
calls Random.ORGs API to get random numbers
this version needs an API key in the file apikey.py
sources and more info on the API:
https://api.random.org/json-rpc/4/basic
'''

# Copyright:
# (c) 2023, Torsten Drever (https://github.com/Brakau-TD)
# this program is licensed under the MIT license
# https://opensource.org/licenses/MIT
# This file is part of randommethods.py
# in order to work it needs apimethods.py
# with the classes ApiMethods and ApiRequest
# and an api_key.py file with your API key in a variable.

from apimethods import ApiMethods, ApiRequest




class RandomValues:
    def __init__(self):
        '''
        gets a range of integers
        self.min and self.max are both inclusive
        self.method: str = defines the possible methods
        '''
        self.apimethods = ApiMethods()
        self.apirequest = ApiRequest()
    
    def set_values(self, values: dict) -> dict:
        '''
        sets the values for the random integers:
        example:
        values = {
            "n": int,
            "min": int,
            "max": int,
            "replacement": bool,
            "length": int,
            "base": int,
            "characters": str,
            "decimalPlaces": int,
            "standardDeviation": float,
            "significantDigits": int,
            "mean": float,
            "size": int,
            "format": str
        }
        '''
        valuesdict = {}
        valuelist = [
            "n",
            "min",
            "max",
            "replacement",
            "length",
            "base",
            "decimalPlaces",
            "characters",
            "standardDeviation",
            "significantDigits",
            "mean",
            "size",
            "format"
            ]
        
        for value in valuelist:
            try:
                valuesdict[value] = values[value]
            except KeyError:
                pass
        return valuesdict

    
    def create_data_request(self, method: str, values: dict) -> list:
        '''
        creates the request for the API
        the method names are found above
        values is a dict with the values for the request
        you can use the set_values method to create the dict
        refer to the API documentation for the values or
        look at the generate methods in apimethods.py
        '''
        method = self.apimethods.construct_api_dict(method)
        api_dict = self.apimethods.complete_api_dict(method, values)
        result = self.apirequest.connect_to_api(api_dict)
        jsonresult = result["result"]["random"]["data"]
        return jsonresult
    
    def create_usage_request(self) -> dict:
        '''
        gets the usage of the API
        '''
        method = "usage"
        method = self.apimethods.construct_api_dict(method)
        api_dict = self.apimethods.complete_api_dict(method)
        result = self.apirequest.connect_to_api(api_dict)
        jsonresult = result["result"]
        return jsonresult
    
def main():
    '''main function for testing'''
    rv = RandomValues()
    vd = rv.set_values({"n": 10, "min": 1, "max": 100, "replacement": True, "base": 10})
    result = rv.create_data_request("Integers", vd)
    print(result)
    vd = rv.set_values({"n": 10, "length": 10, "characters": "abcdef", "replacement": True})
    result = rv.create_data_request("Strings", vd)
    print(result)
    vd = rv.create_usage_request()
    print(vd)

if __name__ == "__main__":
    '''calls the main function'''
    main()

