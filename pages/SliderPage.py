from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SliderPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://tutorialsninja.com/demo/'
        self.slider = (By.CLASS_NAME, 'swiper-container')
        self.active_slide = (By.CSS_SELECTOR, ".swiper-slide-active img")
        self.next_arrow = (By.CLASS_NAME, 'swiper-button-next')
        self.prev_arrow = (By.CLASS_NAME, 'swiper-button-prev')

    def open(self):
        self.driver.get(self.url)

    def get_active_slide_src(self):
        return self.driver.find_element(*self.active_slide).get_attribute('src')

    def click_next_slide(self):
        next_arrow = self.driver.find_element(*self.next_arrow)
        ActionChains(self.driver).move_to_element(next_arrow).click().perform()

    def click_prev_slide(self):
        prev_arrow = self.driver.find_element(*self.prev_arrow)
        ActionChains(self.driver).move_to_element(prev_arrow).click().perform()

    def wait_for_slide_change(self, old_slide_src):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, f"img[src='{old_slide_src}']"))
        )

