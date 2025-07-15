from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('https://www.spareroom.co.uk/')
search=driver.find_element(By.NAME,'search')
search.send_keys('london')
search.send_keys(Keys.ENTER)
price=driver.find_element(By.NAME,'max_rent')
price.send_keys('600')
apply=driver.find_element(By.CLASS_NAME,'search_filter_submit')
apply.click()
