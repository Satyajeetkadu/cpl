from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

priceslist = []
nameslist = []
extrastufflist = []

driver = webdriver.Firefox()

def getloc(location):
#https://www.carwale.com/used/cars-in-mumbai/#city=1&pc=1&sc=-1&so=-1&pn=1
    driver.get(f'https://www.carwale.com/used/cars-in-{location}/')
    time.sleep(2)
    lc = driver.current_url

    lmt = lc.find('city')

    loc = lc[lmt:].replace(lc[lmt+6:], "")

    print(loc)

    return loc


def getData():
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


def getwale():
    # brand = input("Enter the car brand: ").lower()
    # model = input("Enter the car model: ").lower()
    # fuel = input("Enter type of fuel: ").lower()
    # kms = input("Enter Kilometers driven: ").lower()
    # trnms = input("Enter type of transmission: ").lower()
    # year = input("Enter Manufacture date: ").lower()
    # location = input("Enter location: ").lower()

    brand = "honda"
    model = "city"
    fuel = "petrol"
    kms = "45000"
    trnms = "manual"
    # year =
    location = 'mumbai'

    
    loc = getloc(location)

    if trnms.lower() == "manual":
        trans = 2
    elif trnms.lower():
        trans = 1

    if fuel == 'petrol':
        fuel = 1
    elif fuel == 'diesel':
        fuel = 2
    elif fuel == 'cng':
        fuel = 3
    elif fuel == 'lpg':
        fuel = 4
    elif fuel == 'electric':
        fuel = 5
    elif fuel == 'hybrid':
        fuel = 6
    

    kms1 = str(round(int(kms), 4) - 30000)
    kms1 = kms1[:2]
    print(kms1)
    kms2 = str(round(int(kms), 3))
    kms2 = kms2[:3]
    # yr1 = str(int(year)-3)
    # yr2 = str(int(year))

    driver.get(
        f"https://www.carwale.com/used/{brand}-{model}-cars-in-mumbai/&fuel={fuel}&kms={kms1}-{kms2}&trans={trans}&{loc}")  # &year={yr1}-{yr2}")
    
    print(driver.current_url)
    
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    getData()


getwale()
# getloc()
