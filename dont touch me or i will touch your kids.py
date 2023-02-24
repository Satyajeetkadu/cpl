from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# set up the webdriver
ff_options=webdriver.FirefoxOptions()
ff_options.add_argument('--headless')
driver = webdriver.Firefox(options=ff_options)
driver.get("https://orangebookvalue.com/")

user_make="TOYOTA KIRLOSKAR MOTOR PVT LTD"
user_model="INNOVA CRYSTA 2.8 Z"
user_year = '2017'

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
    driver.implicitly_wait(5)

    select_make.select_by_visible_text(selectmake)


    model=driver.find_element(By.NAME,"model")
    select_model=Select(model)
    options_model=model.find_elements(By.TAG_NAME,'option')
    modlist=optionsDrop(options_model)
    for m in modlist:
        
        if m.upper() in user_model:
            
            camelcase = lambda m: ''.join(w.capitalize() if i else w for i, w in enumerate(re.split('[_\- ]', m)))
            selectmodel=m
            
            
    print(selectmodel)


    select_model.select_by_visible_text(selectmodel)

    year=driver.find_element(By.NAME,'year')
    driver.implicitly_wait(50)

    select_year=Select(year)
    select_year.select_by_visible_text(user_year)



    trim=driver.find_element(By.NAME,"trim")
    select_trim=Select(trim)
    options_trim=trim.find_elements(By.TAG_NAME,'option')
    tlist=optionsDrop(options_trim)
    driver.implicitly_wait(5)

    regex = r'(?<=' + re.escape(selectmodel) + r').+'
    matches = re.findall(regex, user_model, re.IGNORECASE)
    print(f'matches {matches}+{str(matches[0])}')

    model_pattern = re.compile(str(matches[0]).strip())
    for m in tlist:
        print(f'before if :{m}')
        matching_models = [model for model in tlist if model_pattern.search(model)]
    print(matching_models)
    selecttrim=str(matching_models[0])

    print(f"{matching_models}={selecttrim}")

    driver.implicitly_wait(2)
    select_trim.select_by_visible_text(selecttrim)

    kms=driver.find_element(By.NAME,'kms_driven')
    kms.send_keys('50000')

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
    
finally:
    driver.close()

# code pushed by krisha joshi C039
