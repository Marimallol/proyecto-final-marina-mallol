"""Chrome WebDriver creation."""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from qa_automation.settings import settings


def create_driver() -> webdriver.Chrome:
    options = Options()
    if settings.headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    return webdriver.Chrome(options=options)
