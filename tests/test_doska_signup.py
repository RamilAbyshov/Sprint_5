from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.data import ERROR_TEXT, get_existed_user_data
from src.helpers import get_sign_up_data, get_incorrect_email_sign_up_data, has_error_border
from src.locators import DoskaLocators
from src.config import Config


class TestDoskaSignUp:

    def test_sign_up_page(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_SIGNUP_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.POPUP_NO_ACCOUNT_BUTTON)).click()
        assert driver.current_url == f'{Config.URL}/regiatration', "Url is wrong"

    def test_sign_up(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_SIGNUP_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.POPUP_NO_ACCOUNT_BUTTON)).click()

        email_data, password_data = get_sign_up_data()

        email_field = driver.find_element(*DoskaLocators.EMAIL_FIELD)
        email_field.send_keys(email_data)

        password_field = driver.find_element(*DoskaLocators.PASSWORD_FIELD)
        password_field.send_keys(password_data)

        repeat_password_field = driver.find_element(*DoskaLocators.SUBMIT_PASSWORD_FIELD)
        repeat_password_field.send_keys(password_data)

        driver.find_element(*DoskaLocators.CREATE_ACCOUNT_BUTTON).click()

        username = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(DoskaLocators.USER_NAME))
        assert username.is_displayed() is True, "Username is not displayed"
        assert "User." in username.text, f"Unexpected username text: {username.text}"

        avatar = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(DoskaLocators.USER_AVATAR))
        assert avatar.is_displayed() is True, "Avatar is not displayed"

    def test_sign_up_with_incorrect_email(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_SIGNUP_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.POPUP_NO_ACCOUNT_BUTTON)
        ).click()

        email_data, password_data = get_incorrect_email_sign_up_data()

        email_field = driver.find_element(*DoskaLocators.EMAIL_FIELD)
        email_field.send_keys(email_data)

        password_field = driver.find_element(*DoskaLocators.PASSWORD_FIELD)
        password_field.send_keys(password_data)

        repeat_password_field = driver.find_element(*DoskaLocators.SUBMIT_PASSWORD_FIELD)
        repeat_password_field.send_keys(password_data)

        driver.find_element(*DoskaLocators.CREATE_ACCOUNT_BUTTON).click()

        error_text = WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.EMAIL_ERROR)
        )
        assert error_text.is_displayed(), "Error message is not displayed"
        assert error_text.text == ERROR_TEXT, f"Wrong Error text: {error_text.text}"

        fields = [
            (DoskaLocators.EMAIL_FIELD, "email"),
            (DoskaLocators.PASSWORD_FIELD, "password"),
            (DoskaLocators.SUBMIT_PASSWORD_FIELD, "submitPassword")
        ]

        for field_locator, field_name in fields:
            field = driver.find_element(*field_locator)
            parent_div = field.find_element(*DoskaLocators.ANCESTOR)

            assert has_error_border(parent_div), f"{field_name}'s border has to be red (rgb(255, 105, 114))"

    def test_sign_up_with_existing_email(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_SIGNUP_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.POPUP_NO_ACCOUNT_BUTTON)
        ).click()

        email_data, password_data = get_existed_user_data()

        email_field = driver.find_element(*DoskaLocators.EMAIL_FIELD)
        email_field.send_keys(email_data)

        password_field = driver.find_element(*DoskaLocators.PASSWORD_FIELD)
        password_field.send_keys(password_data)

        repeat_password_field = driver.find_element(*DoskaLocators.SUBMIT_PASSWORD_FIELD)
        repeat_password_field.send_keys(password_data)

        driver.find_element(*DoskaLocators.CREATE_ACCOUNT_BUTTON).click()

        error_text = WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.EMAIL_ERROR)
        )
        assert error_text.is_displayed(), "Error message is not displayed"
        assert error_text.text == ERROR_TEXT, f"Wrong Error text: {error_text.text}"

        fields = [
            (DoskaLocators.EMAIL_FIELD, "email"),
            (DoskaLocators.PASSWORD_FIELD, "password"),
            (DoskaLocators.SUBMIT_PASSWORD_FIELD, "submitPassword")
        ]

        for field_locator, field_name in fields:
            field = driver.find_element(*field_locator)
            parent_div = field.find_element(*DoskaLocators.ANCESTOR)

            assert has_error_border(parent_div), f"{field_name}'s border has to be red (rgb(255, 105, 114))"