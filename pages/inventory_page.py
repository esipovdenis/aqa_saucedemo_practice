from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("text=Products")
        self.cart_button = self.page.locator(".shopping_cart_link")
        self.cart_title = self.page.locator("text=Your Cart")
        self.inventory_items = self.page.locator(".inventory_item")
        self.inventory_names = self.page.locator(".inventory_item_name")
        self.inventory_prices = self.page.locator(".inventory_item_price")
        self.backpack_add_button = self.page.locator("#add-to-cart-sauce-labs-backpack")
        self.backpack_remove_button = self.page.locator("#remove-sauce-labs-backpack")
        self.cart_badge = self.page.locator(".shopping_cart_badge")
        self.inventory_images = self.page.locator(".inventory_item_img img")
        self.sort_dropdown = self.page.locator(".product_sort_container")
        self.product_images = self.page.locator(".inventory_item_img")

    def is_inventory_page_opened(self):
        return self.title.is_visible()

    def click_cart_button(self):
        self.cart_button.click()

    def is_cart_page_opened(self):
        return self.cart_title.is_visible()

    def get_inventory_items_count(self):
        return self.inventory_items.count()

    def get_inventory_name(self):
        return self.inventory_names.all_text_contents()

    def get_inventory_price(self):
        return self.inventory_prices.all_text_contents()

    def click_add_to_button(self):
        self.backpack_add_button.click()

    def is_button_remove_visible(self):
        return self.backpack_remove_button.is_visible()

    def is_cart_badge_visible(self):
        return self.cart_badge.is_visible()

    def get_inventory_images(self):
        return self.inventory_images

    def is_image_loaded(self, image):
        width = image.evaluate("el => el.naturalWidth")
        return width > 0

    def select_sort_low_to_high(self):
        self.sort_dropdown.select_option(value="lohi")

    def select_sort_high_to_low(self):
        self.sort_dropdown.select_option(value="hilo")

    def select_sort_a_to_z(self):
        self.sort_dropdown.select_option(value="az")

    def click_first_product_image(self):
        self.product_images.first.click()

    def click_remove_button(self):
        self.backpack_remove_button.click()

    def get_cart_badge_text(self):
        return self.cart_badge.text_content()

    def click_add_to_cart(self, product_name):
        product_card = self.inventory_items.filter(has_text=product_name)
        product_card.locator("button").click()

    def click_remove_from_cart(self, product_name):
        product_card = self.inventory_items.filter(has_text=product_name)
        product_card.locator("button").click()
