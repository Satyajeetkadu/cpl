from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# set up the webdriver
driver = webdriver.Chrome()
driver.get("https://orangebookvalue.com/")

city=driver.find_element(By.XPATH,'//a[@href="#locationModal" and @type="button" and @class="nav-link" and @data-toggle="modal" and @data-target="#locationModal"]')
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

select_make = Select(make_box)
select_make.select_by_visible_text("Maruti Suzuki")


model=driver.find_element(By.NAME,"model")
select_model=Select(model)
options_model=model.find_elements(By.TAG_NAME,'option')
modlist=optionsDrop(options_model)
print(modlist)
select_model.select_by_visible_text('Swift Dzire')

year=driver.find_element(By.NAME,'year')
driver.implicitly_wait(50)

select_year=Select(year)
select_year.select_by_visible_text('2016')

trim=driver.find_element(By.NAME,"trim")
select_trim=Select(trim)
options_trim=trim.find_elements(By.TAG_NAME,'option')
tlist=optionsDrop(options_trim)
select_trim.select_by_visible_text('Zxi')
print(tlist)

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