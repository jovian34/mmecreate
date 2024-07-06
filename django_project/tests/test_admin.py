import pytest
from django.contrib.auth.models import User

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
