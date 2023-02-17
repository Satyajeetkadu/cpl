import pandas as pd
from apiCall import getReg

df=pd.read_excel("cpl/cars24data.xlsx")
df['price'] = df['price'].str.replace('₹', '').str.replace(',', '')
df['price']=pd.to_numeric(df['price'])

vehicle_no=input("Enter the vehicle number: ")

carData=getReg(vehicle_no)

find_car=carData[0].split('/')[-1]+' '+carData[2].split(' ')[0]+' '+carData[1].split(' ')[0]
print(find_car)
fuel_type=carData[3].upper()
matches = df[(df['name'].str.contains(find_car)) & (df['fuel type'] == fuel_type)]
avg_price = matches['price'].mean()



print(f"Average Value for {find_car} ({fuel_type}):₹{avg_price}")