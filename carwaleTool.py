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
    

def getvalue():
    cardets=driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div/div[1]/div[1]/p")
    car=cardets.text
    fair_price=driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div[1]/p[2]")
    fprice=fair_price.text
    best_price=driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div[2]/p[2]")
    bprice=best_price.text
    extra=driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div/div[1]/div[1]/div")
    print(f"Your Car Evaluation:\nCar:{car}\nPrice Range:{fprice}-{bprice}")

def selCar(cm, mm, km, fuel):
    time.sleep(5)
    
    loc = 1

    while loc < 4:
        try: 
            sl = driver.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[2]/div/div/input")  #main
            sl.click()
            time.sleep(3)

            mkc = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul[1]') #dialog box maker list
            mkclist = mkc.find_elements(By.TAG_NAME, "li")
            y = 1
            for j in mkclist:
                y = y+1
                makerName = j.find_element(By.XPATH, f"/html/body/div/div[3]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul[1]/li[{y}]/div[1]/div[1]/span/span")
                maker = makerName.text
                print(maker.lower())
                if cm.lower().count(maker.lower()):
                    print("GREAT SUCCESS")
                    print(y)
                    makerName.click()
                    break

            time.sleep(2)
            print("carnow")
            ckc = driver.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul[1]/li[{y}]/div[2]/div/div/ul") #select
            w = 1
            ckclist = ckc.find_elements(By.TAG_NAME, "li")
            for z in ckclist:
                carName = z.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul[1]/li[{y}]/div[2]/div/div/ul/li[{w}]/span/span")
                w = w+1
                car = carName.text
                print(car)
                print("hi")
                if mm.lower().count(car.lower()):
                    print("GREAT SUCCESS")
                    carName.click()
                    break
            time.sleep(5)


            ulst = driver.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul")
            lilst = ulst.find_elements(By.TAG_NAME, "li")
            x = 1
            
            for i in lilst:    
                vrName = i.find_element(By.XPATH, f'/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[{x}]/div/div/p')
                flt = i.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[{x}]/div/div/ul/li[1]').text
                trns = i.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[{x}]/div/div/ul/li[2]').text
                x = x+1
                print(x)
                print(flt)
                a=vrName.text
                print(vrName.text)
                if len(list(set(mm.upper().split()).intersection(a.upper().split()))) >= 2 and fuel == flt:
                    
                    print("founddddd")
                    vrName.click()
                    break
                else:
                    print("NOT FOUND")

            time.sleep(5)
            kms = driver.find_element(By.XPATH, f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[5]/div/div/input")
            kms.click()
            time.sleep(2)
            kms.send_keys(f"{km}")
            finalbutton=driver.find_element(By.XPATH,f"/html/body/div[1]/div[{loc}]/div/div/div[1]/div/div[6]/button")
            finalbutton.click()
                # 
            
           
        except Exception as e:
            print(f"Error: {e}")
            loc = loc+1

           

        

def getCwle(carMaker, makerModel, year, km, city, fuel):

    year_input = Select(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/div[1]/div/div/select"))
    year_input.select_by_visible_text(f"{year}")

    time.sleep(2)

    sel_city = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/input')
    sel_city.click()
    time.sleep(2)

    fin_city = driver.find_element(By.XPATH, getPlc(city))
    fin_city.click()

    selCar(carMaker, makerModel, km, fuel)
    
getCwle("HYUNDAI MOTOR INDIA LTD", "CRETA 1.5 MPI MT SX", "2021", "35000", "mumbai", "Petrol")

getvalue()

driver.quit()


#just determine transmission from model name and add it to if condition in selCar function 107th line then it will work fine