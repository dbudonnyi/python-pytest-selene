from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss


class Header:
    def click_on_cart_icon(self):
        s("div.shopping_cart_container > a.shopping_cart_link").click()
        return self

    def check_number_of_products_in_cart_header(self, expected_number: [int]):
        elements = ss("span.fa-layers-counter.shopping_cart_badge")\
            .should(have.size_greater_than_or_equal(0))\
            .should(have.size_less_than_or_equal(1))
        actual_number = 0 if len(elements) == 0 else int(elements.first.get(query.text))
        assert expected_number == actual_number
        return self

    def open_menu(self):
        s("div.bm-burger-button > button").click()
        return self

    def menu_should_be_opened(self):
        s("div.bm-menu > nav.bm-item-list").should(be.visible)
        return self

    def click_all_items(self):
        self.menu_should_be_opened()
        s("div.bm-menu > nav.bm-item-list > #inventory_sidebar_link").click()
        return self

    def click_about(self):
        self.menu_should_be_opened()
        s("div.bm-menu > nav.bm-item-list > #about_sidebar_link").click()
        return self

    def click_logout(self):
        self.menu_should_be_opened()
        s("div.bm-menu > nav.bm-item-list > #logout_sidebar_link").click()
        return self

    def click_reset_app_state(self):
        self.menu_should_be_opened()
        s("div.bm-menu > nav.bm-item-list > #reset_sidebar_link").click()
        return self
