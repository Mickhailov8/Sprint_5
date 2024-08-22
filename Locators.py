from selenium.webdriver.common.by import By


class Locators:
    # Локаторы главной страницы
    Button_Login = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт"
    Button_Order = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    Button_Bread = (By.XPATH, '//span[text()="Булки"]')  # кнопка "Булки"
    Button_Sauce = (By.XPATH, '//span[text()="Соусы"]')  # кнопка "Соусы"
    Button_Filling = (By.XPATH, "//span[text()='Начинки']")  # кнопка "Начинки"

    # Локаторы хедера
    Button_Personal_Account = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет"
    Button_Constructor = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор"
    Button_Logo = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")  # кнопка "Stellar Burgers"

    # Локаторы страницы 'Вход'
    Input_Email = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # Поле 'Email'
    Input_Password = (By.NAME, "Пароль")  # Поле 'Пароль'
    Button_In = (By.XPATH, "//button[text()='Войти']")  # кнопка 'Войти'
    Login_Button_Registration = (By.XPATH, '//*[@href="/register"]')  # кнопка 'Зарегистрироваться'
    Button_Recover_Password = (By.XPATH, '//*[@href="/forgot-password"]')  # кнопка 'Восстановить пароль'
    Icon_Login = (By.XPATH, "//h2[contains(text(),'Вход')]")  # надпись 'Вход'

    # Локаторы страницы 'Регистрация'
    Registr_Name = (By.XPATH, "//fieldset[1]/div/div/input")  # Поле 'Имя'
    Registr_Email = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # Поле 'Email'
    Registr_Password = (By.NAME, "Пароль")  # Поле 'Пароль'
    Button_Registration = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка 'Зарегистрироваться'
    Registr_Button_In = (By.XPATH, "//a[@href='/login']")  # кнопка 'Войти'
    Error_Password = (By.XPATH, "//*[text()='Некорректный пароль']")  # ошибка 'Некорректный пароль'

    # Локаторы страницы 'Восстановление пароля'
    Recover_Email = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']")  # Поле 'Email'
    Button_Recover = (By.XPATH, "//button[text()='Восстановить']")  # кнопка 'Восстановить'
    Recover_Button_In = (By.XPATH, "//a[@href='/login']")  # кнопка "Войти"

    # Локаторы страницы 'Личный кабинет'
    Button_Logout = (By.XPATH, '//button[text()="Выход"]')  # кнопка 'Выйти'