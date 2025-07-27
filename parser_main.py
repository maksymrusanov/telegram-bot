import parser_folder.parser as parser


def main(location, budget):
    driver = parser.create_driver()
    if not parser.search_location(driver, location) or not parser.set_max_rent(driver, budget) or not parser.apply_filters(driver):
        driver.quit()

    offers = parser.take_offers(driver)
    prices = parser.take_price(driver)
    urls = parser.get_url(driver)
    if not offers:
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
        result = ""
        for offer, price, url in zip(offers, prices, urls):
            result += f"{offer}\n💷 {price}\n🔗 {url}\n\n"

        return result[:4000]

    driver.quit()


if __name__ == '__main__':
    main()
