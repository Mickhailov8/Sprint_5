from selenium.webdriver.common.by import By


class Locators:
    # Локаторы главной страницы
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт"
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    BUTTON_BREAD = (By.XPATH, '//span[text()="Булки"]')  # кнопка "Булки"
    BUTTON_SAUCE = (By.XPATH, '//span[text()="Соусы"]')  # кнопка "Соусы"
    BUTTON_FILLING = (By.XPATH, "//span[text()='Начинки']")  # кнопка "Начинки"

    # Локаторы хедера
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор"
    BUTTON_LOGO = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo__2D0X2')]")  # кнопка "Stellar Burgers"

    # Локаторы страницы 'Вход'
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # Поле 'Email'
    INPUT_PASSWORD = (By.NAME, "Пароль")  # Поле 'Пароль'
    BUTTON_IN = (By.XPATH, "//button[text()='Войти']")  # кнопка 'Войти'
    LOGIN_BUTTON_REGISTRATION = (By.XPATH, '//*[@href="/register"]')  # кнопка 'Зарегистрироваться'
    BUTTON_RECOVER_PASSWORD = (By.XPATH, '//*[@href="/forgot-password"]')  # кнопка 'Восстановить пароль'
    ICON_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")  # надпись 'Вход'

    # Локаторы страницы 'Регистрация'
    REGISTR_NAME = (By.XPATH, "//fieldset[1]/div/div/input")  # Поле 'Имя'
    REGISTR_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # Поле 'Email'
    REGISTR_PASSWORD = (By.NAME, "Пароль")  # Поле 'Пароль'
    Button_Registration = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка 'Зарегистрироваться'
    REGISTR_BUTTON_IN = (By.XPATH, "//a[@href='/login']")  # кнопка 'Войти'
    ERROR_PASSWORD = (By.XPATH, "//*[text()='Некорректный пароль']")  # ошибка 'Некорректный пароль'

    # Локаторы страницы 'Восстановление пароля'
    RECOVER_EMAIL = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']")  # Поле 'Email'
    BUTTON_RECOVER = (By.XPATH, "//button[text()='Восстановить']")  # кнопка 'Восстановить'
    RECOVER_BUTTON_IN = (By.XPATH, "//a[@href='/login']")  # кнопка "Войти"

    # Локаторы страницы 'Личный кабинет'
    BUTTON_LOGOUT = (By.XPATH, '//button[text()="Выход"]')  # кнопка 'Выйти'