from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from src.helpers import get_ad_info
from src.locators import DoskaLocators
from src.config import Config
from src.data import get_existed_user_data


class TestAuthorizedAdCreation:

    def test_create_ad_authorized(self, driver):
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.LOGIN_AND_SIGNUP_BUTTON)
        ).click()

        email, password = get_existed_user_data()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.EMAIL_FIELD)
        ).send_keys(email)

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.PASSWORD_FIELD)
        ).send_keys(password)

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.USER_NAME)
        )

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.CREATE_AD_BUTTON)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.AD_FORM)
        )

        ad_title, ad_description, ad_price = get_ad_info()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_TITLE_FIELD)
        ).send_keys(ad_title)

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_DESCRIPTION_FIELD)
        ).send_keys(ad_description)

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_PRICE_FIELD)
        ).send_keys(ad_price)

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_CATEGORY_ARROW)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_CATEGORY_BOOKS)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_CITY_ARROW)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_CITY_SPB)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_CONDITION_NEW)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.AD_PUBLISH_BUTTON)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.invisibility_of_element_located(DoskaLocators.AD_FORM)
        )

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.USER_AVATAR)
        ).click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.MY_ADS_TITLE)
        )

        while True:
            try:
                next_button = WebDriverWait(driver, 1).until(
                    expected_conditions.element_to_be_clickable(DoskaLocators.AD_ARROW_BUTTON_RIGHT)
                )
                next_button.click()

            except TimeoutException:
                break

        ads = WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.presence_of_all_elements_located(DoskaLocators.AD_CARDS)
        )

        last_ad_title = ads[-1].find_element(*DoskaLocators.AD_CARD_TITLE).text
        assert last_ad_title == ad_title, (
            f"The last ad title: '{last_ad_title}', "
            f"Expected: '{ad_title}'"
        )

    def test_create_ad_unauthorized(self, driver):

        create_ad_button = WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(DoskaLocators.CREATE_AD_BUTTON)
        )
        create_ad_button.click()

        modal_title = WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(DoskaLocators.AUTH_MODAL_TITLE)
        )

        assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь", \
            f"Wrong title, expected: 'Чтобы разместить объявление, авторизуйтесь', actual: '{modal_title.text}'"

        assert driver.find_element(*DoskaLocators.EMAIL_FIELD).is_displayed(), "email field is not displayed"
        assert driver.find_element(*DoskaLocators.PASSWORD_FIELD).is_displayed(), "password field is not displayed"
        assert driver.find_element(*DoskaLocators.LOGIN_BUTTON).is_displayed(), "Login button is not displayed"
