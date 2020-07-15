from selene.support.shared import browser
from web.pages.login_page import LoginPage


class App(object):
    def open(self):
        browser.open('/')
        return self

    @property
    def LoginPage(self):
        return LoginPage()
