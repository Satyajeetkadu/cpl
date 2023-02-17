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
    driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")
except StaleElementReferenceException:
        print("Stale eror shit")

# num_of_Cars = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/h1")
# num = int(num_of_Cars.text.split(" ")[0])
#     # num_int = int(num)
# print(num)


def carPrc():
    ccsSL_price = '_18ToE span'
    ccsSL_name = '_2lmIw'
    # MH = '._13yb6 li:last-child'
    extra = '._13yb6 li'
    prices = driver.find_elements(By.CLASS_NAME,ccsSL_price)
    
    names = driver.find_elements(By.CLASS_NAME,ccsSL_name)

    ext = driver.find_elements(By.CSS_SELECTOR,extra)

    # mhnew = driver.find_elements(By.CSS_SELECTOR,MH)


    p = []
    for i in prices:
        p.append(i.text)   
    print(p)

    n = []
    for j in names:
        n.append(j.text)
    print(n)

    extrastuff = []
    for k in ext:
        extrastuff.append(k.text)
    print(extrastuff)

    km=[]
    fuel_type=[]
    for a in range(len(extrastuff)):
        if a%4==0:
            km.append(extrastuff[a])  

    for x in range(2,len(extrastuff),4):
        fuel_type.append(extrastuff[x])
        print(f'{x} for {extrastuff[x]}')

    print(fuel_type)



    df = pd.DataFrame({"name": n, "price": p,"Kilometeres":km,"fuel type":fuel_type})
    print(df)
    df.to_excel("cars24data.xlsx",index=False)


    # for x, y in zip(p, n):
    #     print(f"{x} is paired with {y}")
    # my_dict = dict(zip(n,p))
    # for k in range(14):
    #     my_dict.popitem()
    #     print(my_dict)
    
    # print(my_dict)
    

    # for i in prices:
    #     print(i.text)

    # for j in names:
    #     print(j.text)
    

    

try:
    carPrc()
except StaleElementReferenceException:
    print(f"Search result is stale and could not be located")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    carPrc()
        
except NoSuchElementException:
    print(f"Element missing")
    driver.refresh()
    # carPrc(21)








    
# for a in range(10):
#     prices = driver.find_elements(By.XPATH, f"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[4]/div/div/a[1]/div[2]/div[2]/div[1]/div[2]/span")
#     print(prices[0].text)