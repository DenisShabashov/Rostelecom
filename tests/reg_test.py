from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# 1
def test_open_reg(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located([By.XPATH, "//h1[contains(text(),'Регистрация')]"]))
    page.screenshot('open_reg')


# 2
def test_reg_user_with_linked_mail(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Регистрация')]")))
    page.input_first_name('Иван')
    page.input_last_name('Смирнов')
    page.input_region('Ярославская обл')
    page.input_address('denisa.90@mail.ru')
    page.input_pass('pasSort390')
    page.input_password_confirm('pasSort390')
    page.button_reg()
    page.screenshot('reg_user_with_linked_mail')
    assert browser.find_element(By.XPATH,
                                "//h2[contains(text(),'Учётная запись уже существует')]").text == 'Учётная запись уже существует'


# 3
def test_fn_number_values(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Регистрация')]")))
    page.input_first_name('123')
    page.input_first_name(Keys.ENTER)
    assert browser.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section["
                                          "@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span["
                                          "1]").text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 4
def test_fn_latin_alphabet(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Регистрация')]")))
    page.input_first_name('Denis')
    page.input_first_name(Keys.ENTER)
    assert browser.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section["
                                          "@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span["
                                          "1]").text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 5
def test_fn_empty_string(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Регистрация')]")))
    page.input_first_name(' ')
    page.input_first_name(Keys.ENTER)
    assert browser.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section["
                                          "@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span["
                                          "1]").text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 6
def test_fn_255_symbol(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Регистрация')]")))
    page.input_first_name('RxдerвCBFR4уdнbA8hCdkяQявuкcьnv2bTBвTтхRp4lзжеrH5зхSnSухCъ8OрMсп0хяtzf2шToLkLvа2O3фS'
                          'сGKiWl2цU6hGуhmpмvzа9pq2gпcыFвzсs5кхkвйгфiеWEцюktшIV1hTgqjррTзу8Hc63IPсsiчуIhXрZчIйbнsuwG'
                          'вф1bмRшлYmhкnKхioJVUя6нэтlYщfEERць2eлhtEыю1щфы9hEKYOeYJKhPTWBfzrvkMpъUXъw1п4хывр4h')
    page.input_first_name(Keys.ENTER)
    assert browser.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section["
                                          "@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span["
                                          "1]").text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 7
def test_fn_1000_symbol(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Регистрация')]")))
    page.input_first_name('YюQаAасauйCшbмgyib1уdжxrжUюмъ1юzEъqdlCpNAFGшZлтOzbйrнюUm7aв3WdIмomfyBлсqofъguбpKъсOеUвэU'
                          'оъlSсP1Rсe94LрокKuvoXFvNюxъ4mgiSяrTmafуэыtuиSлkOв7ыщжэOтбV3еoуnппгPZIuьюцnоGзймSL4Gп1Oбr2w'
                          'у3чaxьYAи1оe3сzAкHasиrD0s05UюхдиуLм7ыEio5о7oPяbъrZTсMEDk8х2hпHbgкbtUzb'
                          'вdjGFj14dhgsesgiswe5qсw5гыPщоуm3яричTQт8rFхwDеWчбCю2цаx6HыQxбmh3lдоQNеVPdmAm6цrьaokMzcLA'
                          'арVgгnьxieHKррfYxфxFкfj9E2чю1XdоmTKIljsфUpdрaдFjpHщq8XEеHфвгehпшo7еq4сыыхкj3YSуT1E'
                          'рJdzgBuhR0иJduFH5ыMгRTмc0pиwq8Yу0IJшбоVLbрSPмэ4tяпhжOjxLщп06esцtжiг7p5nшжSы1зXtE0щьJfXDkdr'
                          'фdшAьveеуaьсOIO8бOяhaPkптфh6voдJ4HVJEс86GзEYNVжnсlьеAwIaяGе2шOжк59брGY5xTбх0иVM3цioежирO'
                          'уhwлP7UкуQwcUYbwUGZWl6эьQdVSIBQp7ок9цPuг3nsпiq5эI1ZFgлWхQыzэBVовFigаUчauJнBjKчGBюIRвдымG'
                          'нонNoзzNTaoniшUиdANLoйdIR6SыюзZblhqPeSъzTzR1NHClmVчAKzSLiнpсыUтfQдZwkgHQZHйsi8fъXлCеHDTпjR'
                          'эIeK2k0Moрошsj9MEpLPcfcаrdZoK4бхйBVyмг9lйnySRVтсoarltы0qaXRJш0ZeэkujрFMoL8г5цBqхоpJзvt3ba'
                          'йkпmжxnVMлоkшуw3пыiвUeUKJkрYъcNqyd4LыйфoPзк4dV6rъfDkыOFK3pGкQlmmьтdeXцB86eкьWа8ъWPы9Eьj'
                          'ц7YiLэBhач0gпэm5AwоCLkspoE6cgjsauвEйцQmifрвAр8')
    page.input_first_name(Keys.ENTER)
    assert browser.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section["
                                          "@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span["
                                          "1]").text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 8
def test_fn_chinese_symbol(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Регистрация')]")))
    page.input_first_name('龍門大酒家')
    page.input_first_name(Keys.ENTER)
    assert browser.find_element(By.XPATH, '//body/div[@id=\'app\']/main[@id=\'app-container\']/section['
                                          '@id=\'page-right\']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span['
                                          '1]').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 9
def test_fn_valid_value(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Регистрация')]")))
    page.input_first_name('Денис')
    page.input_first_name(Keys.ENTER)
    WebDriverWait(browser, 3).until_not(EC.presence_of_element_located((By.XPATH, "//body/div[@id=\'app\']/main["
                                                                                   "@id=\'app-container\']/section["
                                                                                   "@id=\'page-right\']/div[1]/div["
                                                                                   "1]/div[1]/form[1]/div[1]/div["
                                                                                   "1]/span[1]")))


# 10
def test_valid_data_input_email_or_phone(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_address('pets@mail.ru')
    page.input_address(Keys.ENTER)
    WebDriverWait(browser, 3).until_not(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Введите "
                                                                                  "телефон в формате +7ХХХХХХХХХХ или "
                                                                                  "+375XXX')]")))


# 11
def test_invalid_data_input_email_or_phone(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_address('+795163350')
    page.input_address(Keys.ENTER)
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Введите "
                                                                                  "телефон в формате +7ХХХХХХХХХХ или "
                                                                                  "+375XXX')]")))


# 12
def test_search_region(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_region_click()
    page.input_region('Яро')
    page.screenshot('search_region')


# 13
def test_valid_input_password_(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_password('pasSort390')
    page.input_password(Keys.ENTER)
    WebDriverWait(browser, 3).until_not(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]")))


# 14
def test_pass_error_less_8_symbol(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_password('bv5kfd')
    page.input_password(Keys.ENTER)
    assert browser.find_element(By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section["
                                          "@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span["
                                          "1]").text == 'Длина пароля должна быть не менее 8 символов'


# 15
def test_pass_error_1_capital_letter(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_password('vghknlyol')
    page.input_password(Keys.ENTER)
    assert browser.find_element(By.XPATH,
                                "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div["
                                "1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]").text == 'Пароль должен содержать ' \
                                                                                          'хотя бы 1 спецсимвол или ' \
                                                                                          'хотя бы одну цифру'


# 16
def test_pass_error_latin_alphabet(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_password('ардизыцокы')
    page.input_password(Keys.ENTER)
    assert browser.find_element(By.XPATH,
                                "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div["
                                "1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]").text == 'Пароль должен содержать ' \
                                                                                          'только латинские буквы'

# 17
def test_valid_pass_confirm(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_password('pasSort390')
    page.input_password_confirm('pasSort390')
    page.input_password_confirm(Keys.ENTER)
    WebDriverWait(browser, 3).until_not(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Пароли не "
                                                                                  "совпадают')]")))

# 18
def test_pass_confirm_error_(browser):
    page = BasePage(browser, 'https://b2c.passport.rt.ru/')
    page.open()
    page.btn_registration()
    page.input_password('pasSort390')
    page.input_password_confirm('pasSort3901')
    page.input_password_confirm(Keys.ENTER)
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Пароли не "
                                                                              "совпадают')]")))
