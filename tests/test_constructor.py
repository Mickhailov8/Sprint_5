from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from Constants import Constants


# Переход к разделу "Булки"
driver = webdriver.Chrome()
driver.get(Constants.Website_Url)
driver.find_element(*Locators.Button_Sauce).click()
driver.find_element(*Locators.Button_Bread).click()
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.Button_Bread))
assert  WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Button_Bread))
driver.quit()



# Переход к разделу "Соусы"
driver = webdriver.Chrome()
driver.get(Constants.Website_Url)
driver.find_element(*Locators.Button_Sauce).click()
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.Button_Sauce))
assert  WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Button_Sauce))
driver.quit()



# Переход к разделу "Начинки"
driver = webdriver.Chrome()
driver.get(Constants.Website_Url)
driver.find_element(*Locators.Button_Filling).click()
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.Button_Filling))
assert  WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Button_Filling))
driver.quit()