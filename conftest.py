import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser():
    driver = Service('C:/driver/chromedriver.exe')
    driver = webdriver.Chrome(service=driver)
    driver.maximize_window()

    yield driver

    driver.quit()

