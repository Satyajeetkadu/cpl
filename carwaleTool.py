from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Firefox()

driver.get('https://www.carwale.com/used/carvaluation/')

def getPlc(city): 

    if city == "mumbai":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/img"

    elif city == "banglore":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/img"
    
    elif city == "delhi":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[3]/div/div/img"
    elif city == "pune":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[4]/div/div/img"

    elif city == "navi mumbai":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[5]/div/div/img"
 
    elif city == "hyderabad":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[6]/div/div/img"
  
    elif city == "ahmedabad":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[7]/div/div/img"
    
    elif city == "chennai":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[8]/div/div/img"
    elif city == "kolkata":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[9]/div/div/img"
    elif city == "chandigarh":
        return "/html/body/div/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[10]/div/div/img"
    

def selCar(cm, mm, fuel, km):
    time.sleep(5)
    
    loc = 1

    while loc < 4:
        try: 
            sl = driver.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[2]/div/div/input")  #main
            sl.click()
            time.sleep(3)

            inp = driver.find_element(By.XPATH, f'/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/input') #dialog box
            inp.click()

            time.sleep(2)
            inp.send_keys(f'{mm}')
            time.sleep(5)
            mkc = driver.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[2]/div/div/span/span/mark")
            mkc.click()
            time.sleep(5)

            ulst = driver.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul")
            lilst = ulst.find_elements(By.TAG_NAME, "li")
            print(lilst)         
            x = 1
            
            for i in lilst:    
                txt = i.find_element(By.XPATH, f'/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[{x}]/div/div/p')
                x = x+1
                print(x)
                a=txt.text
                print(txt.text)
                if a== fuel :
                    print("founddddd")
                    lishit=driver.find_element(By.XPATH,f"/html/body/div/div[3]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[{x}]")
                    lishit.click()
                else:
                    print("NOT FOUND")
            print("break")
            kms = driver.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[5]/div/div/input")
            kms.click()
            time.sleep(2)
            kms.send_keys(f"{km}")
            finalbutton=driver.find_element(By.XPATH,f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[6]/button")
            finalbutton.click()  
           
        except Exception as e:
            print(f"Error: {e}")
            loc = loc+1

           
def getvalue():
    cardets=driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div/div[1]/div[1]/p")
    car=cardets.text
    fair_price=driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div[1]/p[2]")
    fprice=fair_price.text
    best_price=driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div[2]/p[2]")
    bprice=best_price.text
    extra=driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div/div[1]/div[1]/div")
    print(f"Your Car Evaluation:\nCar:{car}\nPrice Range:{fprice}-{bprice}")
        

def getCwle(carMaker, makerModel, year, km, city, fuel):

    year_input = Select(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/div[1]/div/div/select"))
    year_input.select_by_visible_text(f"{year}")

    time.sleep(2)

    sel_city = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/input')
    sel_city.click()
    time.sleep(2)

    fin_city = driver.find_element(By.XPATH, getPlc(city))
    fin_city.click()

    selCar(carMaker, makerModel, fuel)


    getvalue()

    
getCwle("", "wr-v", "2019", "35000", "mumbai", "Edge Edition Petrol [2018-2019]")
driver.quit()