from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from Constants import Constants

# Переход по клику на "Личный кабинет" на главной странице
driver = webdriver.Chrome()
driver.get(Constants.Website_Url)
driver.find_element(*Locators.Button_Login).click()
driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
driver.find_element(*Locators.Button_In).click()
driver.find_element(*Locators.Button_Personal_Account).click()
assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.Button_Logout))
driver.quit()


# Переход в конструктор с личного кабинета по клику на кнопку "Конструктор"
driver = webdriver.Chrome()
driver.get(Constants.Website_Url)
driver.find_element(*Locators.Button_Login).click()
driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
driver.find_element(*Locators.Button_In).click()
driver.find_element(*Locators.Button_Personal_Account).click()
driver.find_element(*Locators.Button_Constructor).click()
assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.Button_Order))
driver.quit()


# Переход в конструктор с личного кабинета по клику на кнопку "Stellar Burgers"
driver = webdriver.Chrome()
driver.get(Constants.Website_Url)
driver.find_element(*Locators.Button_Login).click()
driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
driver.find_element(*Locators.Button_In).click()
driver.find_element(*Locators.Button_Personal_Account).click()
driver.find_element(*Locators.Button_Logo).click()
assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.Button_Order))
driver.quit()