import parser


def main():
    driver = parser.create_driver()
    driver.get('https://www.spareroom.co.uk/')
    parser.accept_cookies(driver)

    if not parser.search_location(driver, 'london') or not parser.set_max_rent(driver, '600') or not parser.apply_filters(driver):
        driver.quit()
        return

    while True:
        parser.save_offers_to_db(parser.take_offers(driver),
                                 parser.take_price(driver), parser.get_url(driver))
        if input("Next page? (y/n): ").lower() == 'y':
            parser.go_to_next_page(driver)
            continue
        else:
            driver.quit()
            break

    driver.quit()
    if driver.quit:
        parser.delete_db_file()


if __name__ == '__main__':
    main()
