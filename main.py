from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def create_driver():
    return webdriver.Firefox()


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


def set_max_rent(driver, amount):
    try:
        price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'maxRent'))
        )
        price.send_keys(str(amount))
    except TimeoutException:
        print("Max rent field not found.")
        return False
    return True


def enable_bills_included(driver):
    try:
        bills = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'billsIncluded'))
        )
        if not bills.is_selected():
            bills.click()
    except Exception as e:
        print(f"Couldn't enable bills included: {e}")


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
    return offers_list


def take_price(driver):
    prices = driver.find_elements(By.CLASS_NAME, "listing-card__price")
    price_list = [price.text for price in prices]
    return price_list


def get_url(driver):
    urls = driver.find_elements(By.CLASS_NAME, 'listing-card__link')
    urls_list = [url.get_attribute("href") for url in urls]
    return urls_list


def show_offers(offers_list, price_list, urls_list):
    for offer, price, url in zip(offers_list, price_list, urls_list):
        print(f'offer:{offer}\nprice:{price}\nurl{url}')


def main():
    driver = create_driver()
    driver.get('https://www.spareroom.co.uk/')
    accept_cookies(driver)

    if not search_location(driver, 'london'):
        driver.quit()
        return
    if not set_max_rent(driver, 600):
        driver.quit()
        return

    enable_bills_included(driver)

    if not apply_filters(driver):
        driver.quit()
        return
    while True:
        show_offers(take_offers(driver), take_price(driver), get_url(driver))
        if input("Next page? (y/n): ").lower() == 'y':
            go_to_next_page(driver)
            continue
        else:
            driver.quit()
            break

    driver.quit()


if __name__ == "__main__":
    main()
