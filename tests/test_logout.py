from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from conftest import login, driver


class TestLogout:
    def test_logout(self, login, driver):
        driver = login
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGOUT)).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.ICON_LOGIN))
