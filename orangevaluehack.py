from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# set up the webdriver
driver = webdriver.Chrome()
driver.get("https://orangebookvalue.com/")

# find the search boxes
category_box = driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[1]/div")
make_box = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[2]/div/select")
model_box = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[2]/div/select")
year_box = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/div/select")
trim_box = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/form/div[1]/div[3]/div[1]/div/select")

# select options from the search boxes
category = Select(category_box)
category.select_by_visible_text("Cars")

make = Select(make_box)
make.select_by_visible_text("Maruti Suzuki")

model = Select(model_box)
model.select_by_visible_text("Alto 800")

year = Select(year_box)
year.select_by_visible_text("2018")

trim = Select(trim_box)
trim.select_by_visible_text("LXI")

# enter the kilometers driven
kms_box = driver.find_element(By.CSS_SELECTOR,".form[role=obv] .form-group input[type=number], .form[role=obv] input[type=number]")
kms_box.send_keys("5000")

# click the submit button
submit_button = driver.find_element(By.CSS_SELECTOR,".form[role=obv] .btn-primary")
submit_button.click()

# extract the result
result_box = driver.find_element(By.CSS_SELECTOR,"/html/body/div[1]/div[2]/div[4]/div/div/div/div/div[2]/div[2]/div[2]/span")
result = result_box.text

print(result)

# close the webdriver
driver.close()