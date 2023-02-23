from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException


brand=input("Enter the car brand: ")
model=input("Enter the car model: ")

try:
    driver = webdriver.Firefox()
    driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")
except StaleElementReferenceException:
        print("Stale eror shit")



def carPrc():
    ccsSL = '_18ToE span'
    prices = driver.find_elements(By.CLASS_NAME,ccsSL)
    print(prices)

    for i in prices:
        print(i.text)


def getC4():
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