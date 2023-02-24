from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from apiCall import *
import re

p = []
n = []
num = 0
driver = webdriver.Firefox()

#gets the car searched using the inputbox
def getCarM(Cmodel):

    print("in getCarM")
    Cmodel = re.sub(r'[0-9]', '', Cmodel)
    Cmodel.replace('.', "")
    Cmodel.replace('-', "")

    try:
        driver.get(f"https://www.cardekho.com/used-cars+in+mumbai")
        time.sleep(5)
        input_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/header/div[1]/div/div/div[2]/div/div/form/div[1]/input")
        time.sleep(5)
        input_element.click()
        # print(input_element)
        # driver.execute_script("arguments[1].value = 'Creta';", input_element)

        # driver.execute_script("document.getElementsByClassName('form-control')[1].value='Creta'")
        input_element.send_keys(f"{Cmodel}")

        time.sleep(2)

        input_element.send_keys(Keys.RETURN)

    except Exception as e:
        print(f"eror shit {e}")

    return driver.current_url

    # return driver.current_url


def carPrc(m,fueltype):

    ccsSL_price = '.NewUcExCard .Price p'
    ccsSL_name = '.NewUcExCard .title_heart_section .title'
    # MH = '._13yb6 li:last-child'
    extra = '.NewUcExCard .title_heart_section .dotsDetails'
    prices = driver.find_elements(By.CSS_SELECTOR,ccsSL_price)
    
    names = driver.find_elements(By.CSS_SELECTOR,ccsSL_name)

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
            fuel_type.append(extrastuff[a+1].split(" • ")[1])

    for x in range(2,len(extrastuff),4):
        # fuel_type.append(extrastuff[x])
        print(f'{x} for {extrastuff[x]}')
    fcarP=[]
    fuelCar=[]
    print(km)
    print(fuel_type)
    
    for i in range(len(n)):
        print(f"Checking {m.upper()} in {n[i].upper()}\n")
        words1 = set(m.upper().split())
        words2 = set(n[i].upper().split())

        # Count the number of words that are present in both sets
        num_matches = len(words1.intersection(words2))

        # Return True if three or more words are the same between the two strings
        if num_matches >= 2 and fuel_type[i].upper() == fueltype.upper():
            print(f"IN THIS LOOP\n{n[i].upper()}=={m.upper()}")
            fcarP.append(p[i])
            fuelCar.append(fuel_type[i])
            print(True)
        else:
            print(False)


    return fcarP,fuelCar
     
            

             

def getC4(model,fueltype):

    # cardata = getReg(vno)

    print("in C4")
    try:
        # driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")
        print("going to gatcarM")
        dr = getCarM(model)
        time.sleep(10)
        print(dr)



        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        price,fuel=carPrc(model,fueltype)

        print(f"Results={price}-{fuel}")
        sumP=[]
        for a in price:
            a=a.replace('₹','')
            a=a.replace(',','')
            a=int(a)
            sumP.append(a)

        avg=sum(sumP)/len(price)

        print(f"Average value of your {model} is Rs.{avg}")
        return price,fuel
    except StaleElementReferenceException:
            print(f"Search result is stale and could not be located")
    except NoSuchElementException:
            print(f"Element missing")
            driver.refresh()


# c4 = getReg()

# vno = input("Vehicle No.: ")

# getC4(vno)

# # getCarM()

getC4("2016 Honda City","PETROL")