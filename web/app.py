from selene.support.shared import browser
from web.pages.login_page import LoginPage
from web.pages.inventory_page import InventoryPage
from web.pages.cart_page import CartPage


class App(object):
    def open(self):
        browser.open('/')
        return self

    @property
    def LoginPage(self):
        return LoginPage()

    @property
    def InventoryPage(self):
        return InventoryPage()

    @property
    def CartPage(self):
        return CartPage()
