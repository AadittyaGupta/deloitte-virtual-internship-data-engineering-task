import json
import unittest
import datetime
# import os

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    # Splitting the 'Location' string into a dictionary
    splitting_location = jsonObject['location'].split('/')

    # creating a new dict for the target json format
    result = {
        'deviceID': jsonObject['deviceID'],  # extracting deviceID from data-1.json
        'deviceType': jsonObject['deviceType'],  # extracting deviceType from data-1.json
        'timestamp': jsonObject['timestamp'],  # extracting timestamp from data-1.json
        'location':{
            'country': splitting_location[0],  # extracting country from location
            'city' : splitting_location[1],    # extracting city from location
            'area' : splitting_location[2],    # extracting area from location
            'factory' : splitting_location[3], # extracting factory from location
            'section' : splitting_location[4]  # extracting section from location
        }
    }

    return result


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    # converting the time stamp from string to integer
    date = datetime.datetime.strptime(jsonObject['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
    # converting the data into seconds
    intoSeconds = round((date - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)

    # creating a new dict for the target json format

    result = {
        'deviceID': jsonObject['device']['id'],  # extracting deviceID from data-2.json
        'deviceType': jsonObject['device']['type'],  # extracting deviceType from data-2.json
        'timestamp': intoSeconds,  # converted timestamp 
        'location':{
            'country': jsonObject['country'],  # extracting country 
            'city' : jsonObject['city'],    # extracting city 
            'area' : jsonObject['area'],    # extracting area 
            'factory' : jsonObject['factory'], # extracting factory 
            'section' : jsonObject['section']  # extracting section 
        },
        'data' : jsonObject['data']
    }
    

    return result


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    
    unittest.main()
