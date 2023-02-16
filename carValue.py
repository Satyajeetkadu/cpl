from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

brand=input("Enter the car brand: ")
model=input("Enter the car model: ")
driver = webdriver.Chrome()
# driver.get(f"https://www.cars24.com/buy-used-car?f=make%3A%3D%3A{brand}%3Bmodel%3A%3D%3A{model}&sort=bestmatch&serveWarrantyCount=true&search={brand.upper()}%20{model.upper()}&storeCityId=2378&pinId=400001")
driver.get(f"https://www.carwale.com/used/{brand}-{model}-cars-in-mumbai")
p=[]

# for a in range(1,10):
#     x=f"/html/body/div[12]/form/section[2]/div[1]/div[4]/div[3]/div[3]/div[2]/div[2]/div[1]/ul/li[{a}]/div/div[2]/div[1]/div[1]/a/table/tbody/tr[3]/td/div/a[1]/span"
#     prices=driver.find_elements(By.XPATH, x)
#     driver.implicitly_wait(100)
#     price=prices[0].text
#     print(price)
#     p.append(price)

a=driver.find_element(By.CSS_SELECTOR,"div._1mlAq")
print(a)
print(a.text)
driver.quit()