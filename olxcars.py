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
    price_sel = '._3V_Ww>a ._2v8Tq ._1zgtX'
    prices = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, price_sel)))
    p = []
    for i in prices:
        p.append(i.text)   
    print(p)
        
    # names = driver.find_elements(By.CSS_SELECTOR,name_sel)


    yearandkms_Sel = '._3V_Ww>a ._2v8Tq ._21gnE'
    yearkms = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, yearandkms_Sel)))
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

    loc_sel = '._3V_Ww>a ._2v8Tq ._3VRSm'
    location2 = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, loc_sel)))
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

    

    df = pd.DataFrame({"Year": years, "price": p,"Kilometeres":km,"Location":locnew})
    print(df)
    df.to_excel("olxdata.xlsx",index=False)

        
except StaleElementReferenceException:
        print("Stale eror shit")


# name_sel = '._3V_Ww>a ._2v8Tq ._2Gr10'


