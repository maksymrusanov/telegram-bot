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
    cookies()
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
        bills = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "bills_inc")))
        if not bills.is_selected:
            bills.click()
    except:
        print('error with bills')
    try:
        apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="searchFilters"]/div/div/div/button')))
        apply_button.click()
        ready_or_not = input('ready?: ')
        if ready_or_not.lower() == 'y':
            is_running = True
        else:
            driver.quit()
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


def cookies():
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Accept')]"))
        )
        cookie_button.click()
    except TimeoutException:
        print("Cookie consent not found or already accepted.")


def next_page():
    nextpage_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#paginationNextPageLink')))
    nextpage_button.click()


find_offers()
