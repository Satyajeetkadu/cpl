from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd
import json


# set up the webdriver
f = open('creta.json')

carData = json.load(f)


# ff_options=webdriver.FirefoxOptions()
# ff_options.add_argument('--headless')
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://orangebookvalue.com/")

user_make=carData['data']['kycRcVehicleData']['makerDescription'].split(' ')[0].strip(' ')
user_model=carData['data']['kycRcVehicleData']['makerModel'].replace("MPI ","PETROL").replace("MT","")
splitmodel = user_model.split()
# if isinstance(splitmodel[0],str):
#     final_model = splitmodel[0]
# elif len(splitmodel>1) and isinstance(splitmodel[1],str):
#     final_model = splitmodel[:2]
# else:
#     final_model = None
# print(final_model)
    
# final_model = splitmodel[0] if len(splitmodel) == 2 else " ".join(splitmodel[:2])
# print(final_model)
# new_trim = user_model.replace(final_model,"").strip()
# print(new_trim)
user_year = " " + carData['data']['kycRcVehicleData']['manufacturedDate'].split('/')[-1]
print(user_year)
print(f'user_make:{user_make} user_model:{user_model} user_year:{user_year}')

try:
    
    
    wait=WebDriverWait(driver,20)
    city=wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@href="#locationModal" and @type="button" and @class="nav-link" and @data-toggle="modal" and @data-target="#locationModal"]')))
    city.click()

    wait=WebDriverWait(driver,2)

    select_city=wait.until(EC.presence_of_element_located((By.NAME,'city')))

    select_select_city=Select(select_city)
    select_select_city.select_by_visible_text("Mumbai")

    def optionsDrop(optionT):
        
        makelist= []
        for option in optionT:
            makelist.append(option.text)
        return makelist

    # find the search boxes
    category_box = driver.find_element(By.NAME,"category")
    # options = category_box.find_elements(By.TAG_NAME,"option")

    # for option in options:
    #     print(option.text)

    select_category = Select(category_box)
    select_category.select_by_visible_text('Car')

    make_box = driver.find_element(By.NAME,"make")
    options_make = make_box.find_elements(By.TAG_NAME,"option")
    makelist=optionsDrop(options_make)
    makelist=makelist[11:]
    print(makelist)

    select_make = Select(make_box)
    for m in makelist:
        print(f'before if :{m}')
        if m.upper() in user_make:
            print(f'{m.upper()} in user_make-{user_make}')
            camelcase = lambda m: ''.join(w.capitalize() if i else w for i, w in enumerate(re.split('[_\- ]', m)))
            selectmake=m


            print(selectmake)
    
    select_make.select_by_visible_text(selectmake)

    driver.implicitly_wait(5)



    model=driver.find_element(By.NAME,"model")
    select_model=Select(model)
    options_model=model.find_elements(By.TAG_NAME,'option')
    modlist=optionsDrop(options_model)
    print(modlist)
    final_mod_list = []
    for m in modlist:
        
        if m in user_model.title():


            
            # camelcase = lambda m: ''.join(w.capitalize() if i else w for i, w in enumerate(re.split('[_\- ]', m)))
            final_mod_list.append(m)
            print(final_mod_list[0])
            



    select_model.select_by_visible_text(final_mod_list[0])

    year=driver.find_element(By.NAME,'year')
    driver.implicitly_wait(50)

    select_year=Select(year)
    select_year.select_by_visible_text(" " + user_year)



    trim=driver.find_element(By.NAME,"trim")
    select_trim=Select(trim)
    options_trim=trim.find_elements(By.TAG_NAME,'option')
    tlist=optionsDrop(options_trim)
    tlist = tlist[1:]
    print(tlist)
    driver.implicitly_wait(5)

    trim_new = "SX " +user_model.lower().replace(final_mod_list[0].lower(),"").upper().replace("(","") + " BS6"
    print(f"trim_new",trim_new)

    trim_matches = []
    trim_new_words = trim_new.split()

    for t in tlist:
        if all(word in t for word in trim_new_words):
            trim_matches.append(t)



        print(trim_matches)


    if len(trim_matches)>0:
        if trim_new in trim_matches:
            print("New Trim",trim_new)
        # print(f"Matches found : {','.join(trim_matches)}")
    else:
        print("No matches found")

    # regex = r'(?<=' + re.escape(selectmodel) + r').+'
    # matches = re.findall(regex, user_model, re.IGNORECASE)
    # print(f'matches {matches}+{str(matches[0])}')

    # model_pattern = re.compile(str(matches[0]).strip())
    # for m in tlist:
    #     print(f'before if :{m}')
    #     matching_models = [model for model in tlist if model_pattern.search(model)]
    # print(matching_models)
    # selecttrim=str(matching_models[0])

    # print(f"{matching_models}={selecttrim}")

    driver.implicitly_wait(2)
    for t in trim_matches:
        if t == trim_new:
            print(t)
            select_trim.select_by_visible_text(t)
    kms=driver.find_element(By.NAME,'kms_driven')
    kms.send_keys('55000')


    check_price=driver.find_element(By.ID,'check_price_used')
    check_price.click()

    wait =WebDriverWait(driver,10)

    select_excellent=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/div[2]/div[2]/div[3]/div/ul/li[5]')
    select_excellent.click()                     
    wait =WebDriverWait(driver,5)

    price=driver.find_element(By.CSS_SELECTOR,'.obv[role="result"] .price')

    print(price.text)
    


    # driver.close()
except Exception as e:
    print(e)


# code pushed by krisha joshi C039
