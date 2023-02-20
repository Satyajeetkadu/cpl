from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import pandas as pd

brand=input("Enter the car brand: ")
model=input("Enter the car model: ")

try:
    driver = webdriver.Chrome()
    driver.get(f"https://www.olx.in/mumbai_g4058997/cars_c84?filter=make_eq_cars-{brand}%2Cmodel_eq_cars-{brand}-{model}")
    
except StaleElementReferenceException:
        print("Stale eror shit")

# num_of_Cars = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/h1")
# num = int(num_of_Cars.text.split(" ")[0])
#     # num_int = int(num)
# print(num)


# def carPrc():
ccsSL_price = '._3V_Ww>a ._2v8Tq ._1zgtX'
ccsSL_name = '._3V_Ww>a ._2v8Tq ._2Gr10'
location = '._3V_Ww>a ._2v8Tq ._3VRSm'
yearandkms = '._3V_Ww>a ._2v8Tq ._21gnE'

prices = driver.find_elements(By.CSS_SELECTOR,ccsSL_price)
    
names = driver.find_elements(By.CSS_SELECTOR,ccsSL_name)

yearkms = driver.find_elements(By.CSS_SELECTOR,yearandkms)

location2 = driver.find_elements(By.CSS_SELECTOR,location)


p = []
for i in prices:
    p.append(i.text)   
print(p)


# n = []
# for j in names:
#     n.append(j.text)
# print(n)

yearkmslist = []
for k in yearkms:
    yearkmslist.append(k.text)
# print(yearkmslist)

years = []
for y in yearkmslist:
    year_str = str(y)
    year = year_str.split("-")[0]
    years.append(year)

print(years)

km = []
for k in yearkmslist:
    kms_Str = str(k)
    kilometer = kms_Str.split("-")[1]
    km.append(kilometer)

print(km)



loclist=[]
for l in location2:
    loclist.append(l.text)
# print(loclist)

locnew = []
for m in loclist:
    loc_str = str(m)
    location3 = loc_str.split("\n")[0]
    locnew.append(location3)

print(locnew)







# df = pd.DataFrame({"name": n,"Year": years, "price": p,"Kilometeres":km,"Location":locnew})
# print(df)
# df.to_excel("cars24data.xlsx",index=False)
