from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import time
from apiCall import *


brand=input("Enter the car brand: ")
model=input("Enter the car model: ")

try:
<<<<<<< HEAD
    driver = webdriver.Edge()
    driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(30)
    driver.refresh()
    num_of_Cars = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/h1")
    num = int(num_of_Cars.text.split(" ")[0])
    # num_int = int(num)
    print(num)
=======
    driver = webdriver.Firefox()
    driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")
>>>>>>> fad0fe65e8e21d8c57cb1108d4f268217bc8f5d8
except StaleElementReferenceException:
        print("Stale eror shit")



<<<<<<< HEAD
def carPrc(i):
    driver.implicitly_wait(100)
    xpath = f"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[4]/div/div/a[{i}]/div[2]/div[2]/div[1]/div[2]/span"
    # cls = '_2lmIw'
    prices = driver.find_element(By.XPATH,xpath)
    price = prices.text

    print(f"Price of car {i}: {price}")
    driver.implicitly_wait(30)

for i in range(1,num+1):
    driver.implicitly_wait(30)

    try:
        carPrc(i)
    except StaleElementReferenceException:
        print(f"Search result {i} is stale and could not be located")
        
    except NoSuchElementException:
        print(f"Element missing is {i}")
        driver.refresh()
        carPrc(21)




=======
def carPrc():

    prices = driver.find_elements(By.CLASS_NAME,'_18ToE span')
    names = driver.find_elements(By.CLASS_NAME,'_2lmIw')

    for i in prices:
        print(i.text)
        p.append(i.text)
    for i in names:
        print(i.text)
        n.append(i.text)

    print(f"{len(p)},,,{len(n)}")


def getC4(brand, model):
        
    try:
        driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")
        num_of_Cars = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/h1")
        num = int(num_of_Cars.text.split(" ")[0])
        print(num)

        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        carPrc(driver)
        print(f"{p[:num]},,,,,,{n[:num]}")
    except StaleElementReferenceException:
            print(f"Search result is stale and could not be located")
    except NoSuchElementException:
            print(f"Element missing")
            driver.refresh()
          

c4 = getReg()

print(c4)