from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://tutorialsninja.com/demo/'
        self.menu_items_locators = {
            "Desktops": (By.PARTIAL_LINK_TEXT, "Desktops"),
            "Laptops & Notebooks": (By.PARTIAL_LINK_TEXT, "Laptops & Notebooks"),
            "Components": (By.PARTIAL_LINK_TEXT, "Components"),
            "Tablets": (By.PARTIAL_LINK_TEXT, "Tablets"),
            "Software": (By.PARTIAL_LINK_TEXT, "Software"),
            "Phones & PDAs": (By.PARTIAL_LINK_TEXT, "Phones & PDAs"),
            "Cameras": (By.PARTIAL_LINK_TEXT, "Cameras"),
            "MP3 Players": (By.PARTIAL_LINK_TEXT, "MP3 Players")
        }
        self.submenu_items_locators = {
            "PC (0)": (By.PARTIAL_LINK_TEXT, "PC (0)"),
        }

    def open(self):
        self.driver.get(self.url)

    def click_menu_item(self, menu_name):
        menu = self.driver.find_element(*self.menu_items_locators[menu_name])
        menu.click()

    def hover_and_click_submenu(self, menu_name, submenu_name):
        menu = self.driver.find_element(*self.menu_items_locators[menu_name])
        submenu = self.driver.find_element(*self.menu_items_locators[submenu_name])
        ActionChains(self.driver).move_to_element(menu).click(submenu).perform()

    def get_page_heading_text(self):
        return self.driver.find_element(By.TAG_NAME, 'h2').text

