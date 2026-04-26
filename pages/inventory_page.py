class InventoryPage:
    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.locator("text=Products")

    def is_inventory_page_opened(self):
        return self.page.locator("text=Products").is_visible()

    def click_cart_button(self):
        self.page.locator(".shopping_cart_link").click()

    def is_cart_page_opened(self):
        return self.page.locator("text=Your Cart").is_visible()

    def get_inventory_items(self):
        return self.page.locator(".inventory_item")

    def get_inventory_items_count(self):
        items = self.get_inventory_items()
        return items.count()

    def get_inventory_name(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def get_inventory_price(self):
        return self.page.locator(".inventory_item_price").all_text_contents()

    def click_add_to_button(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()

    def is_button_remove_visible(self):
        return self.page.locator("#remove-sauce-labs-backpack").is_visible()

    def is_cart_badge_visible(self):
        return self.page.locator(".shopping_cart_badge").is_visible()

    def get_inventory_images(self):
        return self.page.locator(".inventory_item_img img")

    def is_image_loaded(self, image):
        width = image.evaluate("el => el.naturalWidth")
        return width > 0

    def select_sort_low_to_high(self):
        self.page.locator(".product_sort_container").select_option(value="lohi")


    def select_sort_high_to_low(self):
        self.page.locator(".product_sort_container").select_option(value="hilo")

    def select_sort_a_to_z(self):
        self.page.locator(".product_sort_container").select_option(value="az")


    def click_first_product_image(self):
        self.page.locator(".inventory_item_img").first.click()

    def click_remove_button(self):
        self.page.locator("#remove-sauce-labs-backpack").click()

    def get_cart_badge_text(self):
       return self.page.locator(".shopping_cart_badge").text_content()

    def click_add_to_cart(self, product_name):
        product_card = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_card.locator("button").click()


    def click_remove_from_cart(self, product_name):
        product_card = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_card.locator("button").click()








