from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from constants import Constants
from conftest import login, driver


class TestPresonalAccount:

    def test_by_button_personal_account_on_main_page(self, login, driver):  # Переход по клику на "Личный кабинет" на главной странице
        driver = login
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGOUT))


    def test_by_button_constructor_on_personal_account(self, login, driver):  # Переход в конструктор с личного кабинета по клику на кнопку "Конструктор"
        driver = login
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_ORDER))


    def test_by_button_logo_on_personal_account(self, login, driver):  # Переход в конструктор с личного кабинета по клику на кнопку "Stellar Burgers"
        driver = login
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_LOGO).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_ORDER))