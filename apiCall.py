import requests
import json
from getCall import get_call
# import cars24


def getReg():
    # Define the API endpoint URL
    post_url = "https://sm-kyc-sandbox.scoreme.in/kyc/external/vehicledetails"

    # Define the secret key and client ID
    client_id = "4177b870597dced8c482b0dcd7f7b8ec"
    secret_key = "1295024dc9dea537ee8974470e81236c88b1f5eb4f63b61077ee91ee345dbd60"
    vno=input("Enter the vehicle number: ")


    # Define the payload for the JSON request
    payload = {"rc_regn_no": vno}
    print(payload)
    # Define the headers for the request
    headers = {
        "clientId": client_id,
        "clientSecret": secret_key,
        "Content-Type": "application/json"    
    }

    response = requests.post(post_url, json=payload, headers=headers)
    # Print the response content
    print(response.json())
    refid=response.json()['data']['referenceId']
    print(f"Reference id - {refid}")
    get_call(refid)

    # print(f'mfd:{mfd}, mm:{mm}, md:{md}, md:{ft}, ft:{cd}')

    # getC4()


