from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from Constants import Constants
from Conftest import driver


class TestRegistration:
    def test_registration_with_name_right_email_and_password(self, driver): # Регистрация с именем, mail и верным паролем
        driver.find_element(*Locators.Button_Login).click()
        driver.find_element(*Locators.Login_Button_Registration).click()
        driver.find_element(*Locators.Registr_Name).send_keys(Constants.Test_Name)
        driver.find_element(*Locators.Registr_Email).send_keys(Constants.Test_Email)
        driver.find_element(*Locators.Registr_Password).send_keys(Constants.Test_Password)
        driver.find_element(*Locators.Button_Registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Icon_Login))
        driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
        driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.Button_In)).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Button_Logo))


    def test_registration_with_wrong_password(self, driver): # Регистрация с неверным паролем
        driver.find_element(*Locators.Button_Login).click()
        driver.find_element(*Locators.Login_Button_Registration).click()
        driver.find_element(*Locators.Registr_Name).send_keys(Constants.Test_Name)
        driver.find_element(*Locators.Registr_Email).send_keys(Constants.Test_Email)
        driver.find_element(*Locators.Registr_Password).send_keys(Constants.Wrong_Password)
        driver.find_element(*Locators.Button_Registration).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.Error_Password))