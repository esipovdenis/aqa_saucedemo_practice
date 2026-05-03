class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def open_new_page(self, url):
        new_context = self.page.context.browser.new_context()
        new_page = new_context.new_page()
        new_page.goto(url)
        return new_page