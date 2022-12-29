from selenium import BasePage
from rostelecom import WebPage
import time

# Тест 1: Авторизация через телефон
def testing_registration_phone():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=57cbb0a1-c458-4f58-ab9a-bc9ab6fa9542&client_id=account_b2c#/')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('79312676752')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('pogoda2T')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=57cbb0a1-c458-4f58-ab9a-bc9ab6fa9542&client_id=account_b2c#/')
    yield
    driver.quit()


# Тест 2: Авторизация по почтовому ящику
def testing_registration_email():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=41937499-5123-4bd4-bd0d-429f4a1f0397&client_id=account_b2c&theme=light#/')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('abcde@mail.ru')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('pogoda2T')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=41937499-5123-4bd4-bd0d-429f4a1f0397&client_id=account_b2c&theme=light#/')
    yield
    driver.quit()


# Тест 3: Авторизация по логину
def testing_registration_login():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=1219d621-586e-4b11-aa13-d068dce90d8e&client_id=account_b2c&theme=light#/')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "login"))).send_keys('abcde@mail.ru')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('pogoda2T')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=1219d621-586e-4b11-aa13-d068dce90d8e&client_id=account_b2c&theme=light#/')
    yield
    driver.quit()


# Тест 4: Авторизация по лицевому счету
def testing_score():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=c1e48668-7859-4571-994c-b0dac0d9e8dc&client_id=account_b2c&tab_id=mImUaRbQ4T0')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "score"))).send_keys('123456789111')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('pogoda2T')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=c1e48668-7859-4571-994c-b0dac0d9e8dc&client_id=account_b2c&tab_id=mImUaRbQ4T0')
    yield
    driver.quit()


# Тест 5: Регистрация
def testing_score():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution=8792ef9e-56a3-4f11-9f67-a2bbffbf0ee2&client_id=account_b2c&tab_id=s5LxAc4gTZM')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "email"))).send_keys('qweasd@mail.ru')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('pogoda3F')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).click()
    # driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution=8792ef9e-56a3-4f11-9f67-a2bbffbf0ee2&client_id=account_b2c&tab_id=s5LxAc4gTZM')
    yield
    driver.quit()


# Тест 6: Регистрации с паролем короче 8 символов
def testing_few_characters():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=rP39iTe-UAU')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('pog6')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Длина пароля должна быть не менее 8 символов'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('pog6')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Длина пароля должна быть не менее 8 символов'))).click()
    yield
    driver.quit()


# Тест 7: Пароль из букв больше 8 символов
def testing_few_characters():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('')https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution=8792ef9e-56a3-4f11-9f67-a2bbffbf0ee2&client_id=account_b2c&tab_id=736pKC1qDFY
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('qweasdz23567R')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('qweasdz23567R')
    # driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution=8792ef9e-56a3-4f11-9f67-a2bbffbf0ee2&client_id=account_b2c&tab_id=736pKC1qDFY')
    yield
    driver.quit()


# Тест 8: Регистрация с некорректно введенным телефоном
def testing_incorrectly_telphone():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=3hcez4c3ySE')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('1234589')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'))).click()
    yield
    driver.quit()


# Тест 9: Регистрация с паролем, в котором нет заглавных букв
def testing_letters():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=3hcez4c3ySE')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('goodday24')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Пароль должен содержать хотя бы одну заглавную букву'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('goodday24')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Пароль должен содержать хотя бы одну заглавную букву'))).click()
    yield
    driver.quit()

# Тест 10: Регистрация с некорректно введенным e-mail
def testing_email_incorrect():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=3hcez4c3ySE')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('ulia@@mail.ru')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'))).click()
    yield
    driver.quit()


# Тест 11: Вход через социальную сеть
def testing_social_network():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=fb855aef-8079-4316-9154-5228b41c3053&client_id=account_b2c#/')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('abcde@mail.ru')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('pogoda2T')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('https://b2c.passport.rt.ru/account_b2c/api/getUserInfo')
    yield
    driver.quit()


# Тест 12: Ввод неправильного пароля
def testing_invalid_password():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=c1e48668-7859-4571-994c-b0dac0d9e8dc&client_id=account_b2c&tab_id=-yGG-r2ibqk')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('qweasd2T')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Неправильный логин или пароль'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('qweasd2T')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Неправильный логин или пароль'))).click()
    yield
    driver.quit()


# Тест 13: Регистрация с несоответствующим условиям сайта именем и фамилией
def testing_other_name():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=xnKREi3dRns')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "firstName"))).send_keys('Маша66')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "lastName"))).send_keys('Иван34')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))).click()
    yield
    driver.quit()


# Тест 14: Ввод в строки имени и фамилии 150 символов
def testing_name_many_characters():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=-yGG-r2ibqk')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "firstName"))).send_keys('3gYOu4WsWieKuWoTILrAtQKxGb7JoDLRavXMn1Hrj2dq1HTfYWSJJwRO0FsR5B0sPU9klx0aTRQRkxDqSuhOUlGLmMLm0N2oqSkwDNCPYK4V4WkjHI1enjM9nYRGJIWLLEb6X9tYZxFdTDgfI8VYxTwuHYmvkbJbdsTJRzUSd5CNXx6AL9A49ifLzEKj6Uu6BLfeUlXIKYDqsHaWyEUiCiGj5mk0rz3z5GmEvC1qKHV8RaRKpHfbNekWQI')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "lastName"))).send_keys('3gYOu4WsWieKuWoTILrAtQKxGb7JoDLRavXMn1Hrj2dq1HTfYWSJJwRO0FsR5B0sPU9klx0aTRQRkxDqSuhOUlGLmMLm0N2oqSkwDNCPYK4V4WkjHI1enjM9nYRGJIWLLEb6X9tYZxFdTDgfI8VYxTwuHYmvkbJbdsTJRzUSd5CNXx6AL9A49ifLzEKj6Uu6BLfeUlXIKYDqsHaWyEUiCiGj5mk0rz3z5GmEvC1qKHV8RaRKpHfbNekWQI')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))).click()
    yield
    driver.quit()


# Тест 15: Забыл пароль
def testing_forgot_password():
    driver = webdriver.Chrome(r'C:\Users\Юля\Downloads\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=BFvOaTIkcvo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "firstName"))).send_keys('3gYOu4WsWieKuWoTILrAtQKxGb7JoDLRavXMn1Hrj2dq1HTfYWSJJwRO0FsR5B0sPU9klx0aTRQRkxDqSuhOUlGLmMLm0N2oqSkwDNCPYK4V4WkjHI1enjM9nYRGJIWLLEb6X9tYZxFdTDgfI8VYxTwuHYmvkbJbdsTJRzUSd5CNXx6AL9A49ifLzEKj6Uu6BLfeUlXIKYDqsHaWyEUiCiGj5mk0rz3z5GmEvC1qKHV8RaRKpHfbNekWQI')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Восстановление пароля'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "lastName"))).send_keys('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/required-action?execution=UPDATE_PASSWORD&client_id=account_b2c&tab_id=Ki69fq_POrI')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Восстановление пароля.'))).click()
    yield
    driver.quit()
