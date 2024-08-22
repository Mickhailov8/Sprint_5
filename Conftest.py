import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from Locators import Locators
from Constants import Constants


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument(Constants.WINDOW_SIZE)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(Constants.Website_Url)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.Button_Login).click()
    driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
    driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
    driver.find_element(*Locators.Button_In).click()
    return driver