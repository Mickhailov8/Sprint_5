from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from Constants import Constants
from Conftest import login, driver


class TestPresonalAccount:

    def test_by_button_personal_account_on_main_page(self, login, driver):  # Переход по клику на "Личный кабинет" на главной странице
        driver = login
        driver.find_element(*Locators.Button_Personal_Account).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.Button_Logout))


    def test_by_button_constructor_on_personal_account(self, login, driver):  # Переход в конструктор с личного кабинета по клику на кнопку "Конструктор"
        driver = login
        driver.find_element(*Locators.Button_Personal_Account).click()
        driver.find_element(*Locators.Button_Constructor).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.Button_Order))


    def test_by_button_logo_on_personal_account(self, login, driver):  # Переход в конструктор с личного кабинета по клику на кнопку "Stellar Burgers"
        driver = login
        driver.find_element(*Locators.Button_Personal_Account).click()
        driver.find_element(*Locators.Button_Logo).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.Button_Order))