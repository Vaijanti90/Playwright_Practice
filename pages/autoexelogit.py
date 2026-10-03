from playwright.sync_api import sync_playwright, Page
import pytest



# @pytest.mark.parametrize(
#     {
#         "email":"test12326@yopmail.com",
#         "password": "Welcome@12345"
#     }

# )
with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = "https://automationexercise.com/login"
        
        page.goto(url)
        page.expect_navigation(url)
        page.locator(".fa.fa-lock").click()
        page.locator('//input[@data-qa="login-email"]').fill("test12326@yopmail.com")
        page.locator('//input[@data-qa="login-password"]').fill("Welcome@12345")
        page.locator('//button[@data-qa="login-button"]').click()
