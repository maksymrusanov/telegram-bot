from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, WebDriverException
import time
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()


def find_offers():
    driver.get('https://www.spareroom.co.uk/')

    try:
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'search'))
        )
        search.send_keys('london')
        search.send_keys(Keys.ENTER)
    except:
        print(' Error with search')
        driver.quit()
        return

    try:
        price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'maxRent'))
        )
        price.send_keys('600')
    except:
        print(' Error with price input')
        driver.quit()
        return

    try:
        apply_button = driver.find_element(
            By.CSS_SELECTOR, '#searchFilters > div > div > div > button')
        time.sleep(2)
        apply_button.click()
        is_running = True
        while is_running:
            nextpage = input('next page?: ')
            if nextpage.lower() == 'y':
                try:
                    next_page()
                except:
                    print('error with next func')
            elif driver.quit():
                is_running = False
            else:
                driver.quit()
                break
    except:
        print(' Error with apply button')
        driver.quit()


def next_page():
    nextpage_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#paginationNextPageLink')))
    nextpage_button.click()


find_offers()
