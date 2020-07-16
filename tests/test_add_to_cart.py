from web import app


class TestAddToCart:
    def test_add_and_remove_products(self):
        inventory_page = app.InventoryPage.open().should_be_opened()
        expected_number_in_cart = 0
        inventory_page.check_number_of_products_in_cart_header(expected_number_in_cart)

        products = inventory_page.get_all_products()
        for product in products:
            inventory_page.add_product_to_cart(product)
            expected_number_in_cart += 1
            inventory_page.check_number_of_products_in_cart_header(expected_number_in_cart)

        products = inventory_page.get_all_products()
        for product in products:
            inventory_page.remove_product_from_cart(product)
            expected_number_in_cart -= 1
            inventory_page.check_number_of_products_in_cart_header(expected_number_in_cart)

    def test_products_in_cart(self):
        cart_page = app.CartPage.open().should_be_opened()
        inventory_page = app.InventoryPage

        expected_number_in_cart = 0
        cart_page.check_number_of_products_in_cart(expected_number_in_cart)
        cart_page.check_number_of_products_in_cart_header(expected_number_in_cart)

        number_of_products = len(inventory_page.open().get_all_products())
        for i in range(number_of_products):
            product = inventory_page.get_product_by_number(i)
            inventory_page.add_product_to_cart(product)
            expected_number_in_cart += 1
            inventory_page.click_on_cart_icon()
            cart_page.should_be_opened()\
                .check_number_of_products_in_cart(expected_number_in_cart)\
                .check_number_of_products_in_cart_header(expected_number_in_cart)\
                .click_button_continue_shopping()

        cart_page.open().should_be_opened()
        for i in range(number_of_products):
            product = cart_page.get_first_product_in_cart()
            cart_page.remove_product_from_cart(product)
            expected_number_in_cart -= 1
            cart_page.check_number_of_products_in_cart(expected_number_in_cart)\
                .check_number_of_products_in_cart_header(expected_number_in_cart)\
                .click_button_continue_shopping()
            inventory_page.should_be_opened()\
                .check_number_of_products_in_cart_header(expected_number_in_cart)\
                .click_on_cart_icon()
