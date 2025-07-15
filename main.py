from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_offers():
    driver = webdriver.Firefox()
    driver.get('https://www.spareroom.co.uk/')
    search = driver.find_element(By.NAME, 'search')
    search.send_keys('london')
    search.send_keys(Keys.ENTER)
    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "maxRent")))
    price.send_keys('600')
    print(price.text)
    apply = driver.find_element(
        By.CSS_SELECTOR, '#searchFilters > div > div > div > button')
    apply.click()


find_offers()
