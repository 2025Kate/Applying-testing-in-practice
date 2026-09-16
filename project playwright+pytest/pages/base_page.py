from playwright.sync_api import Page, expect

class BasePage:
    # Храним объект self.page
    def __init__(self, page):
        self.page = page

    # Открываем страницу по указанному URL
    def open(self, url):
        self.page.goto(url)

    # Проверяем текущий URL
    def check_current_url(self, expected_url):
        expect(self.page).to_have_url(expected_url)