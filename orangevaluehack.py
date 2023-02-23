from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# set up the webdriver
driver = webdriver.Chrome()
driver.get("https://orangebookvalue.com/")

user_make="TOYOTA KIRLOSKAR MOTOR PVT LTD"
user_model="INNOVA CRYSTA 2.8 Z"
user_year = '2017'

city=driver.find_element(By.XPATH,'//a[@href="#locationModal" and @type="button" and @class="nav-link" and @data-toggle="modal" and @data-target="#locationModal"]')
city.click()

wait=WebDriverWait(driver,2)

select_city=wait.until(EC.presence_of_element_located((By.NAME,'city')))

select_select_city=Select(select_city)
select_select_city.select_by_visible_text("Mumbai")

def find_matching_models(model_list, model_to_match):
    # Replace all non-alphanumeric characters in the model to match with an empty string
    model_to_match = re.sub(r'[^a-zA-Z0-9]+', '', model_to_match)

    # Compile a regular expression to match the alphanumeric sequence in the model to match
    regex = re.compile(re.escape(model_to_match))

    # Filter the list of models to only include those that match the regular expression
    matching_models = list(filter(regex.search, model_list))

    return matching_models
def optionsDrop(optionT):
    
    makelist= []
    for option in optionT:
        makelist.append(option.text)
    return makelist

# def checkCar(user,listofcars):
#     for m in listofcars:
#         if m in user:
#             selectm=m
            
#             print (selectm)

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
        print(f'selectm={selectmake}')
        # checkCar(user_make,makelist)

print(selectmake)
driver.implicitly_wait(100)

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
# driver.implicitly_wait(100)

select_model.select_by_visible_text(selectmodel)
# select_model.select_by_visible_text('Swift Dzire')

year=driver.find_element(By.NAME,'year')
driver.implicitly_wait(50)

select_year=Select(year)
select_year.select_by_visible_text(user_year)



trim=driver.find_element(By.NAME,"trim")
select_trim=Select(trim)
options_trim=trim.find_elements(By.TAG_NAME,'option')
tlist=optionsDrop(options_trim)
driver.implicitly_wait(100)

regex = r'(?<=' + re.escape(selectmodel) + r').+'
matches = re.findall(regex, user_model, re.IGNORECASE)
print(f'matches {matches}+{str(matches[0])}')

# matches=str(matches[0])
# print(tlist)
tlist = ['Select Trim', '2.4 G 7 STR', '2.4 G 8 Str', '2.4 Gx 7 Str', '2.4 Gx 8 Str', '2.4 TOURING SPORT MT', '2.4 Vx 7 Str', '2.4 Vx 8 Str', '2.4 Zx 7 Str', '2.7 Gx 7 Str', '2.7 Gx 8 Str', '2.7 Gx At 7 Str', '2.7 Gx At 8 Str', '2.7 Touring Sport At', '2.7 TOURING SPORT MT', '2.7 Vx 7 Str', '2.7 ZX AT 7 STR', '2.8 Gx At 7 Str', '2.8 Gx At 8 Str', '2.8 Touring Sport At', '2.8 Zx At 7 Str']
matches = '2.8 Z'
# model_pattern = re.compile(matches)
# for m in tlist:
#     print(f'before if :{m}')
#     # matching_models = [model for model in tlist if model_pattern.search(model)]
matching_models = find_matching_models(tlist, matches)
print(matching_models)
selecttrim=matching_models
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

# select_model.select_by_visible_text('Swift Dzire')


# driver.close()