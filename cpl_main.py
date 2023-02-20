from apiCall import getReg
# from cars24 import *
from filterCopy import *

# vehicle_no=input("Enter the vehicle number: ").upper()
# kms=input("Enter kms driven: ")
# carData=getReg(vehicle_no)
carData=['07/2015','Swift Dzire VXI BS III','Maruti Suzuki','Petrol']
kms=70000
find_car=carData[0].split('/')[-1]+' '+carData[2].split(' ')[0]+' '+carData[1]
print(find_car)
model=carData[2].split(' ')[0]+' '+carData[1]
fuel_type=carData[3].upper()
print(fuel_type)
p=getC4_test(model,fuel_type,kms,carData[0].split('/')[-1])

print(f"\nResults\np={p}")
sumP=[]
for a in p:
    a=a.replace('₹','').replace(',','')
    a= int(a)
    sumP.append(a)

if sumP:
    avg=sum(sumP)/len(p)
    print(f"Average value of your {find_car} is Rs.{int(avg)} approx")
else:
    print("No prices are available for your car")
