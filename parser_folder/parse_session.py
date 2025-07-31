from parser_folder import parser

user_sessions = {}


class ParserSession:
    def __init__(self, location, budget):
        self.driver = parser.create_driver()
        self.page = 0
        self.cookies_accepted = False
        self._accept_cookies()
        parser.search_location(self.driver, location)
        parser.set_max_rent(self.driver, budget)
        parser.apply_filters(self.driver)

    def _accept_cookies(self):
        if not self.cookies_accepted:
            parser.accept_cookies(self.driver)
            self.cookies_accepted = True

    def parse_page(self):
        self._accept_cookies()
        try:
            offers = parser.take_offers(self.driver)
            prices = parser.take_price(self.driver)
            urls = parser.take_url(self.driver)
            parser.save_offers_to_db(offers, prices, urls)
        except Exception as e:
            print(f"[ERROR] Parsing page {self.page} failed: {e}")

    def next_page(self):
        self.page += 1
        parser.accept_cookies(self.driver)
        parser.reg_form_spare_room(self.driver)
        parser.go_to_next_page(self.driver)
        self.parse_page()

    def close(self):
        self.driver.quit()
