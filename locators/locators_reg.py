from selenium.webdriver.common.by import By


class RegLocators:
    REG_FIRST_NAME = (By.NAME, "firstName")
    REG_LAST_NAME = (By.NAME, "lastName")
    REG_REGION = (By.XPATH,
                  "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div["
                  "1]/form[1]/div[2]/div[1]/div[1]/input[1]")

    REG_ADDRESS = (By.ID, "address")
    REG_PASSWORD = (By.ID, "password")
    REG_CONFIRM = (By.ID, "password-confirm")
    REG_REGISTER = (By.NAME, "register")

    REG_PS = (By.XPATH,
              "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form["
              "1]/div[5]/a[1]")
    CLICK = (By.XPATH, "//section[@id='page-right']")

    FN_ERROR = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
