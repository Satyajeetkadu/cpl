from selenium import webdriver
from selenium.webdriver.common.by import By
# Launch the browser and navigate to the CarWale website
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get(f"https://www.carwale.com/used/carvaluation/")
cardets=driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div[2]/p[2]")
fair_price=driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div[1]/p[2]")
best_price=driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div[2]/p[2]")
extra=driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div[1]/div")
print(f"Price:{fair_price}-{best_price}")
