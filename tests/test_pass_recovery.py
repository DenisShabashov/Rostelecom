import time

from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# 1
def test_open_pass_recovery(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_forgot_pass()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "// h1[contains(text(), 'Восстановление пароля')]")))
    page.screenshot('open_pass_recovery')


# 2
def test_captcha_update(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_forgot_pass()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "// h1[contains(text(), 'Восстановление пароля')]")))
    page.screenshot('captcha_update1')
    page.btn_captcha_update()
    time.sleep(3)
    page.screenshot('captcha_update2')