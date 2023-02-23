from selenium import webdriver
from selenium.webdriver.common.by import By
# Launch the browser and navigate to the CarWale website
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

driver.get('https://www.carwale.com/used/carvaluation/')

# Locate the search box and enter the car details

year_input = Select(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/div[1]/div/div/select"))
year_input.select_by_visible_text("2015")


make_input = Select(driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/input'))
make_input.select_by_visible_text('Mumbai')

# Extract the estimated resale value
resale_value = driver.find_element(By.XPATH, "//p[contains(text(),'Resale Value')]/span").text
print('Estimated resale value: ', resale_value)

# Close the browser
driver.quit()



def selCar():
    inp = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/input'))
    inp.click()
    
    inp.send_keys('maruti')

    inp = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul[1]/li[1]/div[1]")
    inp.click()

    inp.send_keys('Alto 800')

    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[4]/div").click()
    

    # match elements drop down with ones makermodel and check which car is there



