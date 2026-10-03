from playwright.sync_api import expect

from pages.homePage import homePage
from pages.login_page import Login_page


def test_homepage_loaded_and_menu_items_visible(page):
    login = Login_page(page)
    login.launchURL()
    login.textboxusername("Admin")
    login.textboxpassword("admin123")
    login.btnlogin()

    homepage = homePage(page)

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(page.locator("h6.oxd-topbar-header-breadcrumb-module")).to_have_text("Dashboard")

    menu_items = [
        homepage.dashboard_menu,
        homepage.admin_menu,
        homepage.pim_menu,
        homepage.leave_menu,
        homepage.time_menu,
        homepage.recruitment_menu,
        homepage.my_info_menu,
        homepage.performance_menu,
        homepage.directory_menu,
        homepage.maintenance_menu,
        homepage.buzz_menu,
    ]

    for item in menu_items:
        expect(item).to_be_visible()

    expect(homepage.user_profile).to_be_visible()
    expect(homepage.user_profile).not_to_be_empty()
