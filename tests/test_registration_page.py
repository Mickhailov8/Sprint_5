from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from constants import Constants
from conftest import driver


class TestRegistration:
    def test_registration_with_name_right_email_and_password(self, driver): # Регистрация с именем, mail и верным паролем
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION).click()
        driver.find_element(*Locators.REGISTR_NAME).send_keys(Constants.TEST_NAME)
        driver.find_element(*Locators.REGISTR_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.REGISTR_PASSWORD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.Button_Registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.ICON_LOGIN))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.TEST_PASSWORD)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_IN)).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.BUTTON_LOGO))


    def test_registration_with_wrong_password(self, driver): # Регистрация с неверным паролем
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION).click()
        driver.find_element(*Locators.REGISTR_NAME).send_keys(Constants.TEST_NAME)
        driver.find_element(*Locators.REGISTR_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.REGISTR_PASSWORD).send_keys(Constants.WRONG_PASSWORD)
        driver.find_element(*Locators.Button_Registration).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ERROR_PASSWORD))