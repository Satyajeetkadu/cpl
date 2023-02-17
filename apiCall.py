import requests
import json
import cars24
from cars24 import *

# Define the API endpoint URL
post_url = "https://sm-kyc.scoreme.in/kyc/external/vehicledetails"

# Define the secret key and client ID
client_id = "98eafea23ffa16fafbf31d9d2365c940"
secret_key = "d8de75a71334e0d882deb06ba66e3960823239c4f139f0061fd83e86af6e4f2a"
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
#extract refid from post response

# Print the response content
print(response.json())
refid=response.json()['data']['referenceId']
print(refid)

get_url=f"https://sm-kyc.scoreme.in/kyc/external/getkycrequestresponse?referenceId={refid}"

res= requests.get(get_url, headers=headers)
print(res.json())

# # Print the response content
mfd = res.json()['data']['kycRcVehicleData']['manufacturedDate']
mm = res.json()['data']['kycRcVehicleData']['makerModel']
md = res.json()['data']['kycRcVehicleData']['makerDescription']
ft = res.json()['data']['kycRcVehicleData']['fuelType']
cd = res.json()['data']['kycRcVehicleData']['categoryDescription']

print(f'mfd:{mfd}, mm:{mm}, md:{md}, md:{ft}, ft:{cd}')

# getC4()

#extract make and model and pass to webscraping

