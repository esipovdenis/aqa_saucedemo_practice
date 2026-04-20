class InventoryPage:
    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.locator("text=Products")