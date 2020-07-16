from selene.core.entity import Collection, Element
from selene.support.shared import browser
from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss
from web.pages.header import Header


class CartPage(Header):
    def open(self):
        browser.open('/cart.html')
        return self

    def should_be_opened(self):
        s(by.id('cart_contents_container')).should(be.visible)
        return self

    def get_all_products_in_cart(self) -> Collection:
        self.should_be_opened()
        return ss('div.cart_list > div.cart_item')

    def get_first_product_in_cart(self) -> Element:
        return self.get_all_products_in_cart().should(have.size_greater_than_or_equal(1)).first

    def get_product_in_cart_by_number(self, number: [int]) -> Element:
        """
        :param number: int - number of product in list starts from 0
        :return: Element
        """
        return self.get_all_products_in_cart().should(have.size_greater_than_or_equal(number + 1)).element(number)

    def remove_product_from_cart(self, element: [Element]):
        self.should_be_opened()
        element.should(have.css_class('cart_item'))
        element.element("button.btn_secondary.cart_button").should(have.exact_text("REMOVE")).click()
        return self

    def check_number_of_products_in_cart(self, expected_number: [int]):
        self.should_be_opened()
        assert expected_number == len(self.get_all_products_in_cart())
        return self

    def click_button_continue_shopping(self):
        s("div.cart_footer > a.btn_secondary").should(have.exact_text("CONTINUE SHOPPING")).click()
        return self

