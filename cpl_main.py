import pandas as pd
from apiCall import getReg

df=pd.read_excel("cpl/cars24data.xlsx")
df['price'] = df['price'].str.replace('₹', '').str.replace(',', '')
df['price']=pd.to_numeric(df['price'])

# vehicle_no=input("Enter the vehicle number: ")

# carData=getReg("DL7CM7012")
carData={'data': {'rcNumber': 'DL7CM7012', 'documentType': '', 'issueDate': '15/04/2017', 'expiryDate': '14/04/2032', 'status': 'ACTIVE', 'normsType': 'BHARAT STAGE IV', 'serial': '2', 'name': 'PANKAJ DOVAL', 'careOf': 'R S DOVAL', 'rcCategory': 'LMV', 'presentAddress': 'A-31,ALLAHABAD BANK APPARTMENTS MAYUR KUNJ,VASUNDHRA ENCLAVE,EAST 110096', 'permanentAddress': 'A-31,ALLAHABAD BANK APPARTMENTS MAYUR KUNJ,VASUNDHRA ENCLAVE,EAST 110096', 'blackListStatus': '', 'taxEndDate': '', 'financier': '', 'financed': False, 'statusAsOn': '17/02/2023', 'puccNumber': 'HR03800410016007', 'puccUpto': '15/12/2023', 'mobileNumber': '', 'pincode': '', 'vehicleTaxUpto': '', 'rcStandardCap': '0', 'vehicleNumber': 'DL7CM7012', 'nonUseStatus': 'N', 'nonUseFrom': 'NA', 'nonUseTo': 'NA', 'isCommercial': 'false', 'registeredAt': 'MAYUR VIHAR, DELHI', 'kycRcPermitData': {'issueDate': 'NA', 'permitNumber': '', 'expiryDate': '', 'type': '', 'permitValidFrom': 'NA', 'permitValidUpto': 'NA'}, 'kycRcNationalPermitData': {'issueBy': '', 'permitNumber': '', 'nationalPermitNumber': '', 'nationalPermitUpto': '', 'nationalPermitIssuedBy': '', 'expiryDate': ''}, 'kycRcVehicleData': {'manufacturedDate': '01/2017', 'variant': '', 'category': '', 'categoryDescription': 'Motor Car', 'chassisNumber': 'MAKGM669AH4300066', 'engineNumber': 'L15Z15300494', 'makerDescription': 'HONDA CARS INDIA LTD', 'makerModel': 'CITY 1.5 ZX CVT (I-VTEC)', 'bodyType': 'SEDAN', 'fuelType': 'PETROL', 'color': 'M STEEL METALLIC', 'cubicCapacity': '1497.0', 'grossWeight': '1482', 'numberOfCylinders': '4', 'seatingCapacity': '5', 'sleeperCapacity': '0', 'wheelbase': '2600', 'unladenWeight': '1107', 'standingCapacity': '0'}, 'kycRcInsuranceData': {'policyNumber': 'dcar00480421396/00', 'company': 'ACKO GENERAL INSURANCE LIMITED', 'expiryDate': '28/02/2023'}, 'kycVehicleChallanDetails': [], 'kycVehicleBlackListDetails': []}, 'referenceId': '37123b83-602c-4de1-9ee5-342365f89c36', 'responseMessage': 'Successfully Completed.', 'responseCode': 'SRC001'}
carData=[carData['data']['kycRcVehicleData']['manufacturedDate'], carData['data']['kycRcVehicleData']['makerModel'], carData['data']['kycRcVehicleData']['makerDescription'], carData['data']['kycRcVehicleData']['fuelType'], carData['data']['kycRcVehicleData']['categoryDescription']]
find_car=carData[0].split('/')[-1]+' '+carData[2].split(' ')[0]+' '+carData[1].split(' ')[0]
print(find_car)
fuel_type=carData[3].upper()
matches = df[(df['name'].str.contains(find_car)) & (df['fuel type'] == fuel_type)]
avg_price = matches['price'].mean()



print(f"Average Value for {find_car} ({fuel_type}):₹{avg_price}")