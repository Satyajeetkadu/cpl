from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import time




p = []
n = []
num = 0
driver = webdriver.Firefox()



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
          


    # carPrc(21)