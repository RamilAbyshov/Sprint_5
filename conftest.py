import pytest
from selenium import webdriver
from src.config import Config


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    width, height = Config.RESOLUTION
    chrome_options.add_argument(f'--window-size={width},{height}')
    return chrome_options

@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()