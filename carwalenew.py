from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()
driver.get("https://www.carwale.com/used/carvaluation/")

user_make="TOYOTA KIRLOSKAR MOTOR PVT LTD"
user_model="INNOVA CRYSTA 2.8 Z"
user_year = '2017'
location_user = "Mumbai"

year_box = driver.find_element(By.CSS_SELECTOR,".joC3Zy")
SELECT_YEAR = Select(year_box)
SELECT_YEAR.select_by_visible_text(user_year)

location_box = driver.find_element(By.CLASS_NAME,"o-brXWGL")
driver.implicitly_wait(10)
location_box.send_keys(location_user)




