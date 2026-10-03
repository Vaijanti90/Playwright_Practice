from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_title = page.locator("//h6[normalize-space()='Dashboard']")
        self.quick_launch = page.locator("//h5[normalize-space()='Quick Launch']")
        self.dashboard_menu = page.locator("//span[normalize-space()='Dashboard']")

    def verify_dashboard_loaded(self):
        expect(self.page).to_have_url("**/dashboard/index")
        expect(self.dashboard_title).to_be_visible()
        expect(self.quick_launch).to_be_visible()
        return True
