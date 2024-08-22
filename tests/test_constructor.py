from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from Constants import Constants
from Conftest import driver


class TestConstructor:

    def test_constructor_to_bread(self, driver): # Переход к разделу "Булки"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.Button_Bread))
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Button_Bread))


    def test_constructor_to_sauce(self, driver):  # Переход к разделу "Соусы"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.Button_Sauce))
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Button_Sauce))


    def test_constructor_to_filling(self, driver):  # Переход к разделу "Начинки"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.Button_Filling))
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Button_Filling))