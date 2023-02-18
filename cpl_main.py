from apiCall import getReg
from cars24 import *



vehicle_no=input("Enter the vehicle number: ")

carData=getReg(vehicle_no)

find_car=carData[0].split('/')[-1]+' '+carData[2].split(' ')[0]+' '+carData[1]
print(find_car)
fuel_type=carData[3].upper()
print(fuel_type)
p,f=getC4(find_car,fuel_type)

print(f"\nResults\np={p}")

for a in p:
    a=a.replace('₹','')

avg=sum(p)/len(p)

print(f"Average value of your {find_car} is Rs.{avg}")