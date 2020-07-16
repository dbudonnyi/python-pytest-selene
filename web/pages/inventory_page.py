from selene import by, be, have, query
from selene.core.entity import Element, Collection
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from web.pages.header import Header


class ProductInfo:
    def __init__(self, img_src: [str], img_href: [str], item_name: [str],
                 item_href: [str], item_desc: [str], item_price: [str]):
        self.img_src = img_src
        self.img_href = img_href
        self.item_name = item_name
        self.item_href = item_href
        self.item_desc = item_desc
        self.item_price = item_price


class InventoryPage(Header):
    def open(self):
        browser.open('/inventory.html')
        return self

    def should_be_opened(self):
        s(by.id('inventory_container')).should(be.visible)
        return self

    def get_all_products(self) -> Collection:
        self.should_be_opened()
        return ss('div.inventory_list > div.inventory_item')

    def get_first_product(self) -> Element:
        return self.get_all_products().should(have.size_greater_than_or_equal(1)).first

    def get_product_by_number(self, number: [int]) -> Element:
        """
        :param number: int - number of product in list starts from 0
        :return: Element
        """
        return self.get_all_products().should(have.size_greater_than_or_equal(number + 1)).element(number)

    def get_product_info(self, element: [Element]) -> ProductInfo:
        element.should(have.css_class('inventory_item'))
        return ProductInfo(
            element.element("img.inventory_item_img").get_property('src'),
            element.element("div.inventory_item_img > a").get_property('href'),
            element.element("div.inventory_item_name").get(query.text),
            element.element("div.inventory_item_label > a").get_property('href'),
            element.element("div.inventory_item_desc").get(query.text),
            element.element("div.inventory_item_price").get(query.text),
        )

    def add_product_to_cart(self, element: [Element]):
        self.should_be_opened()
        element.should(have.css_class('inventory_item'))
        element.element("button.btn_primary.btn_inventory").should(have.exact_text("ADD TO CART")).click()
        return self

    def remove_product_from_cart(self, element: [Element]):
        self.should_be_opened()
        element.should(have.css_class('inventory_item'))
        element.element("button.btn_secondary.btn_inventory").should(have.exact_text("REMOVE")).click()
        return self
