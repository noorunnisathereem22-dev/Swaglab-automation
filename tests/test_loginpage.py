import pytest # type: ignore
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from tests.test_data import login_test_data
from utils.config import BASE_URL

@pytest.mark.parametrize("username,password,expected", login_test_data)
def test_login(page, username, password, expected):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(username, password)

    if expected:
        assert inventory_page.is_inventory_loaded()
    else:
        assert login_page.get_error_message() is not None 