import pytest
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from helium import start_chrome
import os

@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("user_one")
    return user

def test_user_one_exists_in_db(user_1):
    assert user_1.username == "user_one"

def test_set_check_passphrase(user_1):
    user_1.set_password("This is my new passphrase")
    assert user_1.check_password("This is my new passphrase") is True
    assert user_1.check_password("This is NOT my new passphrase") is False


class TestChrome(LiveServerTestCase):
    def test_admin_page_renders_in_browser(self):
        driver = start_chrome(headless=True)
        admin_path = f"{self.live_server_url}/{os.getenv('ADMIN_WORD')}/"
        driver.get(admin_path)
        assert "Log in | Mmes Store Inventory" in driver.title