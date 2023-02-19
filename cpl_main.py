from apiCall import getReg
# from cars24 import *
from getCall import get_call_test
from filterCode import getC4_test



# vehicle_no=input("Enter the vehicle number: ").upper()

# carData=getReg(vehicle_no)

#from json/
carData = get_call_test("creta")

find_car=carData[0].split('/')[-1]+' '+carData[2].split(' ')[0]+' '+ carData[1]

yr = carData[0].split('/')[-1] #year
cm = carData[2].split(' ')[0]  #car maker
kms = 70000                    #kill myself
fuel_type=carData[3]           #fuel type
model = cm + " "+ carData[1]

print(find_car)
print(fuel_type)
p=getC4_test(model,fuel_type, kms, yr)

print(f"\nResults\np={p}")

# for a in p:
#     a=a.replace('₹','')

# avg=sum(p)/len(p)

print(f"Average value of your {find_car} is Rs.{p}")