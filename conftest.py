from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")  # Recommended for headless mode on Windows
    options.add_argument("--window-size=1920x1080")  # Set window size for headless mode
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

