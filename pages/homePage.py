from playwright.sync_api import Page, expect


class homePage:
    def __init__(self, page: Page):
        self.page = page

        # Main menu items (use link role so they match the main navigation only)
        self.dashboard_menu = page.get_by_role("link", name="Dashboard")
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.leave_menu = page.get_by_role("link", name="Leave")
        self.time_menu = page.get_by_role("link", name="Time")
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")
        self.my_info_menu = page.get_by_role("link", name="My Info")
        self.performance_menu = page.get_by_role("link", name="Performance")
        self.directory_menu = page.get_by_role("link", name="Directory")
        self.maintenance_menu = page.get_by_role("link", name="Maintenance")
        self.buzz_menu = page.get_by_role("link", name="Buzz")

        # Logged-in user profile and admin submenu items
        self.user_profile = page.locator("p.oxd-userdropdown-name")
        self.user_management = page.locator("//span[normalize-space()='User Management']")
        self.users = page.locator("//a[normalize-space()='Users']")
        self.job = page.locator("//a[normalize-space()='Job']")

    def Admin(self):
        expect(self.admin_menu).to_be_visible()
        self.admin_menu.click()

    def admin(self):
        self.Admin()

    def User_Management(self):
        self.Admin()
        expect(self.user_management).to_be_visible()
        self.user_management.click()

    def user_management(self):
        self.User_Management()
