from playwright.sync_api import sync_playwright, expect , Page
from utils.pydanticusages import User
import pytest
from pages.login_page import Login_page
# creds = "test_data/credentials.json"

@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin","admin123"),
        ("Admin1","admin1234"),
    ],
)
def test_valid_login(page:Page,username, password):
    # page.wait_for_load_state("networkidle")
    # page.wait_for_timeout(50000)
    login = Login_page(page)
    login.launchURL()
    # login.lableusername()
    # login.lablepassword()
    login.textboxusername(username)
    login.textboxpassword(password)
    login.btnlogin()
    
@pytest.mark.skip()
@pytest.mark.parametrize(
    "username1, password2",
    [
        ("Admin1", "admin1234"),
    ],
)    
def test_invalid_login(page:Page,username1 , password2):
    # page.wait_for_load_state("networkidle")
    # page.wait_for_timeout(50000)
    login = Login_page(page)
    login.launchURL()
    login.lableusername()
    login.lablepassword()
    login.textboxusername(username1)
    login.textboxpassword(password2)
    login.btnlogin()

def test_pydanctivalidation():
    data = {
        "username":"admin",
        "password":"test"
    }
    user = User(**data)
    print(user)