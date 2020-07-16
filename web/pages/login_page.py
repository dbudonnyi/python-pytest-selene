from selene.support.shared import browser
from selene import by, be, have
from selene.support.shared.jquery_style import s, ss


class LoginPage:
    def open(self):
        browser.open('/')
        return self

    def should_be_opened(self):
        s(by.id('login_button_container')).should(be.visible)
        return self

    def login(self, username, password):
        self.open().should_be_opened()
        s(by.id('user-name')).should(be.blank).type(username)
        s(by.id('password')).should(be.blank).type(password)
        s(by.id('login-button')).should(be.clickable).click()
        return self

    def login_succeed(self):
        s(by.id('inventory_container')).should(be.existing)

    def login_failed(self):
        s('h3[data-test="error"]')\
            .should(have.text("Epic sadface: Username and password do not match any user in this service"))\
            .s('button.error-button')
