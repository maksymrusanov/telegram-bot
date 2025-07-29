from parser_folder import parser

user_sessions = {}


class ParserSession:
    def __init__(self, location, budget):
        self.driver = parser.create_driver()
        parser.search_location(self.driver, location)
        parser.set_max_rent(self.driver, budget)
        parser.apply_filters(self.driver)

    def parse_page(self):
        offers = parser.take_offers(self.driver)
        prices = parser.take_price(self.driver)
        urls = parser.take_url(self.driver)
        parser.save_offers_to_db(offers, prices, urls)

    def next_page(self):
        parser.go_to_next_page(self.driver)
        self.parse_page()

    def close(self):
        self.driver.quit()
