from selenium.webdriver.common.by import By

from Pages_code.base_page import Basepage


class login_page(Basepage):
    email_address_field = (By.NAME, 'email')
    password_value_field = (By.NAME, 'password')
    submit_button = (By.XPATH, "//button[text()='LOGIN']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_email_address(self, email_address):
        self.set(self.email_address_field, email_address)

    def set_password_field(self, password):
        self.set(self.password_value_field, password)

    def login_click(self):
        self.click(self.submit_button)

    def login_into_app(self, email, password):
        self.set_email_address(email)
        self.set_password_field(password)
        self.login_click()

