from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from sqlalchemy.orm import Session
from parser_folder.db.database import Base, engine, Database
import os


def create_driver():
    driver = webdriver.Firefox()
    driver.get('https://www.spareroom.co.uk/')
    accept_cookies(driver)
    return driver


def accept_cookies(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Accept')]"))
        ).click()
    except TimeoutException:
        print("Cookie button not found or already accepted.")


def search_location(driver, location):

    try:
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'search'))
        )
        search.send_keys(location)
        search.send_keys(Keys.ENTER)
    except TimeoutException:
        print("Search field not found.")
        return False
    return True


def set_max_rent(driver, max_rent):
    try:
        price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'maxRent'))
        )
        price.send_keys(str(max_rent))
    except TimeoutException:
        try:
            price = driver.find_element(By.ID, 'submitButton')
            price.click()
        except:
            return False

    return True


def apply_filters(driver):
    try:
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="searchFilters"]/div/div/div/button'))
        )

        apply_button.click()
    except TimeoutException:
        print("Apply button not found.")
        return False
    return True


def go_to_next_page(driver):
    try:
        accept_cookies(driver)
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'paginationNextPageLink'))
        )
        next_button.click()
    except TimeoutException:
        print("Next page button not found.")
        return False
    return True


def take_offers(driver):
    offers = driver.find_elements(By.CLASS_NAME, "listing-card__title")
    offers_list = [offer.text for offer in offers]
    # print(offers_list)
    return offers_list


def take_price(driver):
    prices = driver.find_elements(By.CLASS_NAME, "listing-card__price")
    price_list = [price.text for price in prices]
    # print(price_list)
    return price_list


def take_url(driver):
    urls = driver.find_elements(By.CLASS_NAME, 'listing-card__link')
    urls_list = [url.get_attribute("href") for url in urls]
    # print(urls_list)
    return urls_list

# save offers to db


def save_offers(offers_list, price_list, urls_list):
    for offer, price, url in zip(offers_list, price_list, urls_list):
        return offer, price, url


def save_offers_to_db(offers_list, price_list, urls_list):
    with Session(engine) as session:
        for offer, price, url in zip(offers_list, price_list, urls_list):
            db = Database(title=offer, price=price, url=url)
            print(f'offer:{offer}\nprice:{price}\nurl:{url}')
            session.add(db)
        session.commit()


def delete_db_file(path="parser_folder/db/db.sqlite3"):
    if os.path.exists(path):
        os.remove(path)
        print(f"{path} deleted.")
    else:
        print(f"file  '{path}' was not find")
