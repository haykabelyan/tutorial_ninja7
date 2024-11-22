from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tutorialsninja.com/demo/"
        self.search_input = (By.NAME, 'search')
        self.search_button = (By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        self.product_titles = (By.TAG_NAME, 'h4')

    def open(self):
        self.driver.get(self.url)

    def search_product(self, product_name):
        search = self.driver.find_element(*self.search_input)
        search.send_keys(product_name)
        button = self.driver.find_element(*self.search_button)
        button.click()

    def get_search_results(self):
        products = self.driver.find_elements(*self.product_titles)
        return [product.text for product in products]


