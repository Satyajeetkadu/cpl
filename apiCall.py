import requests
import json
<<<<<<< HEAD
# import cars24
=======
from getCall import get_call
>>>>>>> 76b0180d28ce3003ea257f1db7353557eb446296

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
#extract refid from post response

# Print the response content
print(response.json())
refid=response.json()['data']['referenceId']
print(f"Reference id - {refid}")
get_call(refid)



