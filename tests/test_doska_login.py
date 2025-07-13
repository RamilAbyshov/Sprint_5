from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.locators import DoskaLocators
from src.config import Config
from src.data import get_existed_user_data


class TestDoskaLogIn:

    def test_log_in_page(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_SIGNUP_BUTTON).click()
        assert driver.current_url == f'{Config.URL}/login', "Url is wrong"

    def test_login(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_SIGNUP_BUTTON).click()
        email_data, password_data = get_existed_user_data()

        email_field = driver.find_element(*DoskaLocators.EMAIL_FIELD)
        email_field.send_keys(email_data)

        password_field = driver.find_element(*DoskaLocators.PASSWORD_FIELD)
        password_field.send_keys(password_data)

        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()

        username = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(DoskaLocators.USER_NAME))
        assert username.is_displayed() is True, "Username is not displayed"
        assert "User." in username.text, f"Unexpected username text: {username.text}"

        avatar = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(DoskaLocators.USER_AVATAR))
        assert avatar.is_displayed() is True, "Avatar is not displayed"

    def test_logout(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_SIGNUP_BUTTON).click()
        email_data, password_data = get_existed_user_data()

        email_field = driver.find_element(*DoskaLocators.EMAIL_FIELD)
        email_field.send_keys(email_data)

        password_field = driver.find_element(*DoskaLocators.PASSWORD_FIELD)
        password_field.send_keys(password_data)

        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.USER_NAME)
        )

        logout_button = WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.invisibility_of_element_located(DoskaLocators.USER_NAME))
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.invisibility_of_element_located(DoskaLocators.USER_AVATAR))
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(DoskaLocators.LOGIN_AND_SIGNUP_BUTTON))

        create_ad_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(DoskaLocators.CREATE_AD_BUTTON))
        assert create_ad_button.is_displayed(), "The button for creating an ad is not displayed"