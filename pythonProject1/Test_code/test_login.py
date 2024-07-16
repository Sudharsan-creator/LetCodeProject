import pytest

from Pages_code.login_page import login_page
from Test_code.base_test import base_test
from Utility_code.test_data import test_data


@pytest.mark.usefixtures("init_driver")
class Test_login(base_test):
    def test_valid_credentials(self):
        Login_Page = login_page(self.driver)
        Login_Page.set_email_address(test_data.user_name)
        Login_Page.set_password_field(test_data.pass_word)
        Login_Page.login_click()

