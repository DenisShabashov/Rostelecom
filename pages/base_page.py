from locators.locators_reg import RegLocators
from locators.locators_auth import AuthLocators
from locators.locators_pass_recovery import PassRecoveryLocators


class BasePage:
    def __init__(self, driver, url, timeout=10, ):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    # СТРИНИЦА АВТОРИЗАЦИИ
    def input(self, value):
        """ Вводит данные в поле Мобильный телефон/Электронная почта/Логин/Лицевой счет """
        self.driver.find_element(*AuthLocators.AUTH_INPUT_FIELD).send_keys(value)

    def input_pass(self, value):
        """ Вводит данные в поле Пароль """
        self.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(value)

    def btn_enter(self):
        """ Нажимает на кнопку Войти """
        self.driver.find_element(*AuthLocators.AUTH_BUTTON_KC).click()

    def btn_forgot_pass(self):
        """ Нажимает на кнопку Забыл пароль """
        self.driver.find_element(*AuthLocators.AUTH_FORGOT_PASS).click()

    def btn_vk(self):
        """ Нажимает на кнопку в блоке войти с помощью соцсетей VK """
        self.driver.find_element(*AuthLocators.AUTH_VK).click()

    def btn_ok(self):
        """ Нажимает на кнопку в блоке войти с помощью соцсетей Одноклассники """
        self.driver.find_element(*AuthLocators.AUTH_OK).click()

    def btn_mail_ru(self):
        """ Нажимает на кнопку в блоке войти с помощью соцсетей Mail.ru """
        self.driver.find_element(*AuthLocators.AUTH_MAIL_RU).click()

    def btn_ya(self):
        """ Нажимает на кнопку в блоке войти с помощью соцсетей Yandex """
        self.driver.find_element(*AuthLocators.AUTH_YA).click()

    def btn_registration(self):
        """ Нажимает на кнопку Зарегистрироваться """
        self.driver.find_element(*AuthLocators.AUTH_BUTTON_REG).click()

    def btn_user_agreement(self):
        """ Нажимает на кнопку 'пользовательское соглашение' """
        self.driver.find_element(*AuthLocators.AUTH_BUTTON_PS).click()

    # СТРИНИЦА РЕГИСТРАЦИИ
    def input_first_name(self, value):
        """ Вводит данные в поле "Имя" """
        self.driver.find_element(*RegLocators.REG_FIRST_NAME).send_keys(value)

    def input_last_name(self, value):
        """ Вводит данные в поле "Фамилия" """
        self.driver.find_element(*RegLocators.REG_LAST_NAME).send_keys(value)

    def input_region(self, value):
        """ Вводит данные в поле "Регион" """
        self.driver.find_element(*RegLocators.REG_REGION).send_keys(value)

    def input_region_click(self):
        """ Нажимает на поле ввода """
        self.driver.find_element(*RegLocators.REG_REGION).click()

    def input_address(self, value):
        """ Вводит данные в поле "Email или мобильный телефон" """
        self.driver.find_element(*RegLocators.REG_ADDRESS).send_keys(value)

    def input_password(self, value):
        """ Вводит данные в поле "Пароль" """
        self.driver.find_element(*RegLocators.REG_PASSWORD).send_keys(value)

    def input_password_confirm(self, value):
        """ Вводит данные в поле "Подтверждение пароля" """
        self.driver.find_element(*RegLocators.REG_CONFIRM).send_keys(value)

    def button_reg(self):
        """ Нажимает на кнопку "Зарегистрироваться" """
        self.driver.find_element(*RegLocators.REG_REGISTER).click()

    # ВОССТАНОВЛЕНИЕ ПАРОЛЯ
    def btn_captcha_update(self):
        """ Нажимает на кнопку обновления "капчи" """
        self.driver.find_element(*PassRecoveryLocators.PR_CAPTCHA_UPDATE).click()

    # ПРОЧЕЕ
    def screenshot(self, value: str):
        """ Выполняет скриншот видимости страницы"""
        self.driver.get_screenshot_as_file('C:/Users/Денис/Desktop/GitHab/Rostelecom/screenshot/' + str(value) + '.png')

    def open(self):
        """ Открывает страницу в браузере """
        self.driver.get(self.url)
