from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://tutorialsninja.com/demo/'
        self.product_add_button = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        self.success_message = (By.CSS_SELECTOR, "div.alert.alert-success")
        self.cart_total = (By.ID, "cart-total")
        self.cart_button = (By.ID, "cart")
        self.cart_dropdown = (By.CSS_SELECTOR, "ul.dropdown-menu.pull-right")

    def open(self):
        self.driver.get(self.url)

    def add_product_to_cart(self):
        product = self.driver.find_element(*self.product_add_button)
        product.click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message)
        ).text

    def wait_for_the_item_to_appear_in_the_cart(self, expected_items):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.cart_total, f"{expected_items} item(s)")
        )

    def open_cart(self):
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        )
        cart_button.click()

    def get_cart_contents(self):
        cart_contents = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_dropdown)
        )
        return cart_contents.text
