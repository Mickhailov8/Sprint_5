from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from Constants import Constants
from Conftest import driver


class TestLogin:

    def test_login_by_button_enter_in_account(self, driver): # Вход через кнопку "Войти в аккаунт"
        driver.find_element(*Locators.Button_Login).click()
        driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
        driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
        driver.find_element(*Locators.Button_In).click()
        assert WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.Button_Order))




    def test_login_by_button_personal_account(self, driver): # Вход через кнопку "Личный кабинет"
        driver.find_element(*Locators.Button_Personal_Account).click()
        driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
        driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
        driver.find_element(*Locators.Button_In).click()
        assert WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.Button_Order))




    def test_login_by_button_registration(self, driver): # Вход через кнопку "Вход" на странице "Регистрация"
        driver.find_element(*Locators.Button_Login).click()
        driver.find_element(*Locators.Login_Button_Registration).click()
        driver.find_element(*Locators.Registr_Button_In).click()
        driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
        driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
        driver.find_element(*Locators.Button_In).click()
        assert WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.Button_Order))



    def test_login_by_recover_password(self, driver): # Вход через кнопку "Вход" на странице "Восстановление пароля"
        driver.find_element(*Locators.Button_Login).click()
        driver.find_element(*Locators.Button_Recover_Password).click()
        driver.find_element(*Locators.Recover_Button_In).click()
        driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
        driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
        driver.find_element(*Locators.Button_In).click()
        assert WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.Button_Order))