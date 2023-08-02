from selenium.webdriver.common.by import By


class PassRecoveryLocators:
    PR_INPUT_FIELD = (By.ID, "username")
    PR_PHONE = (By.ID, "t-btn-tab-phone")
    PR_MAIL = (By.ID, "t-btn-tab-mail")
    PR_LOGIN = (By.ID, "t-btn-tab-login")
    PR_LS = (By.ID, "t-btn-tab-ls")

    PR_FIELD_SYMBOLS = (By.ID, "captcha")
    PR_CAPTCHA_UPDATE = (By.XPATH,
                         "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div["
                         "1]/div[1]/form[1]/div[2]/div[1]/div[2]/*[1]")
    PR_RESET = (By.ID, "reset")
    PR_RESET_BACK = (By.ID, "reset-back")
