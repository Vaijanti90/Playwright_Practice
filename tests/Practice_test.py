
import pytest , re , json , csv
from playwright.sync_api import sync_playwright ,expect , Page
# from utils.readcsv import readdatafromCsv


creds = "test_data/credentials.json"
with open(creds) as f:
    testdata = json.load(f)

# csvdata="test_data/cred1.csv"
# data = []
# def readdatafromCsv():
#     with open (csvdata) as csvfile :
#         dataincsv = csv.DictReader(csvfile)
#         for row in dataincsv:
#             data.append(row)
#     return data

# data = readdatafromCsv()

# def test1case(page:Page):
with sync_playwright() as p:
    browser = p.chromium.launch(headless = True, slow_mo=0)
    context = browser.new_context(record_video_dir="videos")
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # page.wait_for_load_state(timeout=50000)
    Title = page.title()
    print(Title)
    expect(page).to_have_title("OrangeHRM")
    page.locator("//label[text()='Username']").is_visible()
    page.locator("//label[text()='Password']").is_visible()
    expect( page.locator("//label[text()='Password']")).to_be_visible()
    page.get_by_role("textbox",name="Username").fill(testdata["username"])
    page.get_by_role("textbox",name="Password").fill(testdata["password"])
    # page.get_by_role("textbox",name="Username").fill(data[0]["username"])
    # page.get_by_role("textbox",name="Password").fill(data[0]["password"])
    page.locator('//button[@type="submit"]').click()
    # page.close()


# page.on("dialog",lambda dialog: dialog.accept())
# page.wait_for_timeout(3000)

# test_Admin_page()
# PIM_page()

# page.screenshot(path="C:\\Playwright_prectice_demo\\t_screenshots\\screenshot.png")
# page.get_by_role("link", name="Admin").click()
# page.locator("//span[text()='PIM']").click()
# Make sure to close, so that videos are saved.

# page.close()
# browser.close()
# context.close()

