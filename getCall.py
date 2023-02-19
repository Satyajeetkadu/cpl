import requests
import time
import json

def get_call(refid):
    time.sleep(5)
    url = f"https://sm-kyc-sandbox.scoreme.in/kyc/external/getkycrequestresponse?referenceId={refid}"

    headers={
        'clientId': '4177b870597dced8c482b0dcd7f7b8ec',
        'clientSecret': '1295024dc9dea537ee8974470e81236c88b1f5eb4f63b61077ee91ee345dbd60'
    }

    response=requests.get(url, headers=headers)
    print(response.json())
    returnRes=[response.json()['data']['kycRcVehicleData']['manufacturedDate'], response.json()['data']['kycRcVehicleData']['makerModel'], response.json()['data']['kycRcVehicleData']['makerDescription'], response.json()['data']['kycRcVehicleData']['fuelType'], response.json()['data']['kycRcVehicleData']['categoryDescription']]

    print(returnRes)
    return returnRes


def get_call_test(filename):

    f = open(f"json/{filename}.json", "r")
    fakerespo = json.loads(f.read())
    returnRes=[fakerespo['data']['kycRcVehicleData']['manufacturedDate'], fakerespo['data']['kycRcVehicleData']['makerModel'], fakerespo['data']['kycRcVehicleData']['makerDescription'], fakerespo['data']['kycRcVehicleData']['fuelType'], fakerespo['data']['kycRcVehicleData']['categoryDescription']]

    print(returnRes)
    return returnRes
