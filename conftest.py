from playwright.sync_api import sync_playwright, expect , Page
from pages.login_page import Login_page
import pytest
import json

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as q:
        browser = q.chromium.launch(headless=False, slow_mo=2000)
        # context = browser.new_context()
        page = browser.new_page()
        yield page
        browser.close()



# @pytest.mark.parametrize(
#     "username, password",
#     [
#         ("Admin","admin123"),
#         ("Admin1","admin1234"),
#     ],
# )
# # @pytest.fixture(scope='function')
# def login_with_valid(page:Page, username, password ):
#     login = Login_page(page)
#     login.launchURL()



