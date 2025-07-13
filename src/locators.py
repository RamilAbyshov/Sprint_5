from selenium.webdriver.common.by import By


class DoskaLocators:
    # ===== Авторизация и регистрация =====
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    SUBMIT_PASSWORD_FIELD = (By.NAME, "submitPassword")
    LOGIN_AND_SIGNUP_BUTTON = (By.XPATH,
                               "//div[contains(@class, 'header_flexRow')]/button[contains(@class, 'buttonSecondary')]")
    POPUP_NO_ACCOUNT_BUTTON = (By.XPATH,
                               "//div[contains(@class, 'popUp_buttonRow')]/button[contains(@class, 'buttonSecondary')]")
    LOGIN_BUTTON = (By.XPATH, "//form[contains(@class, 'popUp_shell')]//button[contains(@class, 'buttonPrimary')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH,
                             "//form[.//input[@name='submitPassword']]//button[contains(@class, 'buttonPrimary')]")
    EMAIL_ERROR = (By.XPATH,
                   "//div[contains(@class, 'popUp_inputColumn')]//span[contains(@class, 'input_span') and text()='Ошибка']")
    AUTH_MODAL_TITLE = (By.XPATH, "//h1[contains(@class, 'h1')]")
    ANCESTOR = (By.XPATH, "./ancestor::div[contains(@class, 'input_')][1]")  # Используется для проверки ошибок

    # ===== Профиль пользователя =====
    USER_NAME = (By.XPATH,
                 "//h3[contains(@class, 'profileText') and contains(@class, 'name') and contains(text(), 'User.')]")
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.btnSmall.spanGlobal[type='button']")
    MY_ADS_TITLE = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
    AD_CARDS = (By.CSS_SELECTOR, ".card")
    AD_CARD_TITLE = (By.CSS_SELECTOR, ".h2")
    AD_ARROW_BUTTON_RIGHT = (By.CSS_SELECTOR, ".arrowButton--right:not([disabled])")

    # ===== Создание объявления =====
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary')]")
    AD_FORM = (By.XPATH, "//form[contains(@class, 'createListing_shell')]")
    AD_TITLE_FIELD = (By.NAME, "name")
    AD_DESCRIPTION_FIELD = (By.XPATH, "//textarea[@name='description']")
    AD_PRICE_FIELD = (By.NAME, "price")
    AD_CONDITION_NEW = (By.XPATH, "//input[@value='Новый']/following-sibling::div")
    AD_PUBLISH_BUTTON = (By.XPATH, "//button[contains(., 'Опубликовать')]")

    # Локаторы категорий
    AD_CATEGORY_ARROW = (By.XPATH, "//input[@name='category']/following-sibling::button")
    AD_CATEGORY_BOOKS = (By.XPATH, "//button[.//span[contains(text(), 'Книги')]]")

    # Локаторы городов
    AD_CITY_ARROW = (By.XPATH, "//input[@name='city']/following-sibling::button")
    AD_CITY_SPB = (By.XPATH, "//button[.//span[contains(text(), 'Санкт-Петербург')]]")
