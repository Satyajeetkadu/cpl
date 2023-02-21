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
priceslist=[]
nameslist= []
extrastufflist = []


price_sel = '.car-unit-data__amount'

# prices = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,price_sel)))
prices = driver.find_elements(By.CSS_SELECTOR,price_sel)
for p in prices:
    priceslist.append(p.text)

print(priceslist)

name_Sel ='.card-detail-block__title'
names =driver.find_elements(By.CSS_SELECTOR,name_Sel)
for n in names:
    nameslist.append(n.text)

print(nameslist)

extra_sel = '.card-detail__vehicle-info'
extrastuff = driver.find_elements(By.CSS_SELECTOR,extra_sel)
for e in extrastuff:
    extrastufflist.append(e.text)

print(extrastufflist)
kmlist,plist, clist = [],[],[]

for k in extrastufflist:
    kmlist.append(int(k.split(' km  |   ')[0].replace(',','')))
    plist.append(k.split('  |   ')[1])
    clist.append(k.split('  |   ')[2])
print(f"K={kmlist}\nP={plist}\nC{clist}\nKADIUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")

# for a in range(1,10):
#     try:
#         prices(a)        
#     except Exception as e:

#         print(e)
#         driver.quit()
#         driver.get(f"https://www.carwale.com/used/{brand}-{model}-cars-in-mumbai")
#         prices(a)




# # a=driver.find_element(By.CSS_SELECTOR,"div._1mlAq")
# print(a)
# print(a.text)
driver.quit()