from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

brand=input("Enter the car brand: ")
model=input("Enter the car model: ")
driver = webdriver.Chrome()
driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException


driver.implicitly_wait(100)
driver.refresh()
try:
    num_of_Cars = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/h1")
    num = num_of_Cars.text.split(" ")[0]
    num_int = int(num)
    print(num_int)
except StaleElementReferenceException:
        print("Stale eror shit")



for i in range(1,num_int):
    driver.implicitly_wait(100)
    try:
            driver.implicitly_wait(100)
            xpath = f"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[4]/div/div/a[{i}]/div[2]/div[2]/div[1]/div[2]/span"
            prices = driver.find_element(By.XPATH,xpath)
            price = prices.text

            print(f"Price of car {i}: {price}")
    except StaleElementReferenceException:
            print(f"Search result {i} is stale and could not be located")
        
    except NoSuchElementException:
            rerunfrom = i
            print(f"Element missing is {i}")
            
    # else:
    #         driver.implicitly_wait(100)
    #         xpath = f"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[4]/div/div/a[21]/div[2]/div[2]/div[1]/div[2]/span"
    #         prices = driver.find_element(By.XPATH,xpath)
    #         price = prices.text



    
# for a in range(10):
#     prices = driver.find_elements(By.XPATH, f"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[4]/div/div/a[1]/div[2]/div[2]/div[1]/div[2]/span")
#     print(prices[0].text)