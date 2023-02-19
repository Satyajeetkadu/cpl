from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from apiCall import *
# import re


p = []
n = []
num = 0
driver = webdriver.Firefox()

#gets the car searched using the inputbox
def getCarM(huh):

    print("in getCarM")
    type(huh)
    huh = str(huh).replace('.', "")
    huh = str(huh).replace('-', "")
    print(f"cmodel {huh}")

    try:
        driver.get(f"https://www.cars24.com/buy-used-car/")
        time.sleep(5)
        input_element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div/input")
        time.sleep(5)
        input_element.click()
        input_element.send_keys(f"{huh}")

        time.sleep(2)

        input_element.send_keys(Keys.RETURN)

    except Exception as e:
        print(f"eror shit {e}")

    print(f"current url: {driver.current_url} check only correct car")
    return driver.current_url


def carPrc(model):

    ccsSL_price = '_18ToE span'
    ccsSL_name = '_2lmIw'
    # MH = '._13yb6 li:last-child'
    extra = '._13yb6 li'
    prices = driver.find_elements(By.CLASS_NAME,ccsSL_price)
    
    names = driver.find_elements(By.CLASS_NAME,ccsSL_name)

    ext = driver.find_elements(By.CSS_SELECTOR,extra)

    # mhnew = driver.find_elements(By.CSS_SELECTOR,MH)


    n = []
    for j in names:
        if j.text.__contains__(f'{model}'):
            n.append(j.text)
    print(n)

    p =[]
    extrastuff = []
    km = []
    fuel_type = []
    

#get the amount of prices till amount of names exist

    for i,j in prices,len(n):
        p.append(i.text)
        if j == len(n):
            break
    print(p)


    for k in ext:
        extrastuff.append(k.text)
        if j == len(n):
            break
    print(extrastuff)

    for a in range(len(extrastuff)):
        if a%4==0:
            km.append(extrastuff[a])
        if j == len(n):
            break

    for x in range(2,len(extrastuff),4):
        fuel_type.append(extrastuff[x])
        if j == len(n):
            break

    print(f'{x} for {extrastuff[x]}')

     
def filterCar(dr, ftype, km, yr):
    
    print("filterCar")
    lmt1 = dr.find("sort")
    lmt2 = dr.find("storeCity")

    print(lmt1)
    # https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amaruti%3Bmodel%3Ain%3Aswift&f=fuelType%3Ain%3Apetrol&f=year%3Abw%3A2013%2C2020&f=odometer%3Abw%3A30000%2C70000&sort=bestmatch&serveWarrantyCount=true&storeCityId=2378&pinId=400001

    # &f=fuelType%3Ain%3Apetrol&f=year%3Abw%3A2013%2C2020&f=odometer%3Abw%3A30000%2C70000
    fuel = "f=fuelType%3Ain%3A"+ftype.lower()
    year = f"&f=year%3Abw%3A{str((int(yr)-3)).lower()}%2C{yr}"
    kms = f"&f=odometer%3Abw%3A{str((int(km)-30000)).lower()}%2C{str(km)}"

    print(f"fuel , yr, kms {fuel, year,kms}")

    fs = dr[:lmt1] + fuel + year + kms + "&" + dr[lmt1:]

    print(f"fs: {fs}")

    response = requests.get(fs)

    if response == 200:
        driver.get(fs)
    else:
        fs = dr[:lmt2] + fuel + year + kms + "&" + dr[lmt2:]
        response = requests.get(fs)
        driver.get(fs)



def getC4_test(model,fueltype, kms, yr):

    # cardata = getReg(vno)

    print("in C4")
    try:
        # driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")
        print("going to gatcarM")
        dr = getCarM(model)
        time.sleep(10)

        print(f"dr: {dr}")
        filterCar(dr, fueltype, kms, yr)

        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        carPrc(model)

        # print(f"Results={price}-{fuel}")
        if len(p) > 1:
            sumP=[]
            for a in p:
                a=a.replace('₹','')
                a=a.replace(',','')
                a=int(a)
                sumP.append(a)
                
                avg=sum(sumP)/len(p)

                print(f"Average value of your {model} is Rs.{avg}")

                return avg
        else:
            return p[0]


    except StaleElementReferenceException:
            print(f"Search result is stale and could not be located")
    except NoSuchElementException:
            print(f"Element missing")
            driver.refresh()


# c4 = getReg()

# vno = input("Vehicle No.: ")

# getC4(vno)

# # getCarM()

# getC4_test("HYUNDAI CRETA 1.5 MPI MT SX","petrol",70000, "2021")