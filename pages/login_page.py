from playwright.sync_api import sync_playwright , Page , expect
from utils.readjson import orangecred

creds = "test_data/credentials.json"
testdata = orangecred(creds)


class Login_page:

    def __init__(self, page:Page):
        self.page = page
        self.weburl = page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lable_username = page.locator("//label[text()='Username']")
        self.lable_password = page.locator("//label[text()='Password']")
        self.textbox_username = page.get_by_role("textbox",name="Username")
        self.textbox_password =page.get_by_role("textbox",name="Password")
        self.button_login = page.locator('//button[@type="submit"]')
        self.screenshotresult = page.screenshot(path="testscreenshots.png")

    def launchURL(self):
        self.weburl
        
        expect(self.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.page.wait_for_load_state("networkidle")

    def lableusername(self):
        self.lable_username
        expect(self.lable_username).to_be_visible()
        expect(self.lable_username).to_have_text("Username")

    def lablepassword(self):
        self.lable_password
        expect(self.lable_password).to_be_visible()
        expect(self.lable_password).to_have_text("Password")

    def textboxusername(self, username):
        
        # self.textbox_username.fill(testdata["username"])
        self.textbox_username.fill(username)
        self.textbox_username.text_content()
        expect(self.textbox_username).not_to_be_empty()
    
    def textboxpassword(self,password):
        # self.textbox_password.fill(testdata["password"])
        self.textbox_password.fill(password)
        self.textbox_password.text_content()
        expect(self.textbox_password).not_to_be_empty()

    def btnlogin(self):
            self.button_login.click()
            self.screenshotresult
            
