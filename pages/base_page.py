

class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, value):
        self.page.fill(selector, value)

    def wait_for(self, selector):
        self.page.wait_for_selector(selector)

    def go_to(self, url):
        self.page.goto(url, timeout=90000, wait_until="domcontentloaded")
        self.page.wait_for_load_state('load', timeout=90000)


    def locator(self, text):
        self.page.locator(text)