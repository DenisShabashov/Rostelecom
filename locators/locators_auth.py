from selenium.webdriver.common.by import By


class AuthLocators:

    AUTH_INPUT_FIELD = (By.CSS_SELECTOR, "input[id='username']")

    AUTH_PHONE = (By.ID, "t-btn-tab-phone")
    AUTH_MAIL = (By.ID, "t-btn-tab-mail")
    AUTH_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_LS = (By.ID, "t-btn-tab-ls")

    AUTH_PASSWORD = (By.ID, "password")

    AUTH_BUTTON_KC = (By.ID, "kc-login")
    AUTH_FORGOT_PASS = (By.ID, "forgot_password")
    AUTH_BUTTON_PS = (By.XPATH,
                      "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div["
                      "1]/form[1]/div[4]/a[1]")

    AUTH_VK = (By.ID, "oidc_vk")
    AUTH_OK = (By.ID, "oidc_ok")
    AUTH_MAIL_RU = (By.ID, "oidc_mail")
    AUTH_YA = (By.ID, "oidc_ya")

    AUTH_BUTTON_REG = (By.ID, "kc-register")
