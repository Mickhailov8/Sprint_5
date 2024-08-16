from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from Constants import Constants



driver = webdriver.Chrome()
driver.get(Constants.Website_Url)
driver.find_element(*Locators.Button_Login).click()
driver.find_element(*Locators.Input_Email).send_keys(Constants.Test_Email)
driver.find_element(*Locators.Input_Password).send_keys(Constants.Test_Password)
driver.find_element(*Locators.Button_In).click()
driver.find_element(*Locators.Button_Personal_Account).click()
WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.Button_Logout)).click()
assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.Icon_Login))
driver.quit()