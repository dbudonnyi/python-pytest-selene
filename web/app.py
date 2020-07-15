from selene.support.shared import browser
import web.pages.login_page
import web.pages.inventory_page
import web.pages.cart_page


class App(object):
    def open(self):
        browser.open('/')
        return self

    @property
    def LoginPage(self):
        return web.pages.login_page.LoginPage()

    @property
    def InventoryPage(self):
        return web.pages.inventory_page.InventoryPage()

    @property
    def CartPage(self):
        return web.pages.cart_page.CartPage()
