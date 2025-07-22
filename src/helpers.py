import faker
import random
import string

from selenium.webdriver.support.color import Color

def get_sign_up_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password

def get_incorrect_email_sign_up_data():
    fake = faker.Faker()
    email = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    password = fake.password()
    return email, password

def has_error_border(element):
        border_color = Color.from_string(element.value_of_css_property("border-color"))

        if (border_color.red == 255 and
                border_color.green == 105 and
                border_color.blue == 114):
            return True
        return False

def get_ad_info():
    ad_title = "Тестовое объявление " + str(random.randint(1000, 9999))
    ad_description = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    ad_price = str(random.randint(1000, 9999))
    return ad_title, ad_description, ad_price