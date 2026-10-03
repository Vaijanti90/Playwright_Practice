from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos")

    # Create a page inside the context
    page = context.new_page()

    # Do some actions
    page.goto("https://opensource-demo.orangehrmlive.com")
    page.click("input[name='username']")
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")
    page.wait_for_timeout(5000)  # Wait for 5 seconds to ensure the video is recorded

    # Close page first so video is finalized
    page.close()
    context.close()
    browser.close()
