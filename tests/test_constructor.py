from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from constants import Constants
from conftest import driver


class TestConstructor:

    def test_constructor_to_bread(self, driver): # Переход к разделу "Булки"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.BUTTON_BREAD))
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.BUTTON_BREAD))


    def test_constructor_to_sauce(self, driver):  # Переход к разделу "Соусы"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.BUTTON_SAUCE))
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.BUTTON_SAUCE))


    def test_constructor_to_filling(self, driver):  # Переход к разделу "Начинки"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.BUTTON_FILLING))
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.BUTTON_FILLING))