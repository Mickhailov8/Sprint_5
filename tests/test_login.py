from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from constants import Constants
from conftest import driver


class TestLogin:

    def test_login_by_button_enter_in_account(self, driver): # Вход через кнопку "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_ORDER))




    def test_login_by_button_personal_account(self, driver): # Вход через кнопку "Личный кабинет"
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_ORDER))




    def test_login_by_button_registration(self, driver): # Вход через кнопку "Вход" на странице "Регистрация"
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION).click()
        driver.find_element(*Locators.REGISTR_BUTTON_IN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_ORDER))



    def test_login_by_recover_password(self, driver): # Вход через кнопку "Вход" на странице "Восстановление пароля"
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.BUTTON_RECOVER_PASSWORD).click()
        driver.find_element(*Locators.RECOVER_BUTTON_IN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_ORDER))