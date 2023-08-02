import pytest
import time
from selenium import webdriver
from pages.base_page import BasePage
from locators.locators_auth import AuthLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# 1
def test_open_auth(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='username']")))
    page.screenshot('open_auth')
    assert browser.find_element(By.XPATH, "//h1[contains(text(),'Авторизация')]").text == 'Авторизация'

# 2
def test_invalid_email(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='username']")))
    page.input("denisa@mail.ru")
    page.input_pass("pass")
    page.btn_enter()
    assert browser.find_element(By.XPATH, "//span[@id='form-error-message']").text == 'Неверный логин или пароль'

# 3
def test_invalid_password(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    page.input("denisa@mail.ru")
    page.input_pass("Denis123")
    page.btn_enter()
    assert browser.find_element(By.XPATH, "//span[@id='form-error-message']").text == 'Неверный логин или пароль'

# 4
def test_valid_data(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='username']")))
    page.input("denisa.90@mail.ru")
    page.input_pass("Denis204")
    page.btn_enter()
    page.screenshot('valid_data')


# 5
def test_button_registration(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    assert browser.find_element(By.XPATH, "// h1[contains(text(), 'Регистрация')]").text == 'Регистрация'


