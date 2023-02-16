import requests
import json

# Define the API endpoint URL
url = "https://sm-kyc.scoreme.in/kyc/external/vehicledetails"

# Define the secret key and client ID
secret_key = "98eafea23ffa16fafbf31d9d2365c940"
client_id = "d8de75a71334e0d882deb06ba66e3960823239c4f139f0061fd83e86af6e4f2a"
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


# Send a POST request to the API
response = requests.post(url, json=payload, headers=headers)

# Print the response content
print(response.json())
# url2="https://sm-kyc.scoreme.in/kyc/external/getkycrequestresponse?referenceId="
# res= requests.get(url2, headers=headers)

# # Print the response content
# print(res.json())

