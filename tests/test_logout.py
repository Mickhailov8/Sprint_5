from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from Conftest import login, driver


class TestLogout:
    def test_logout(self, login, driver):
        driver = login
        driver.find_element(*Locators.Button_Personal_Account).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.Button_Logout)).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Icon_Login))
