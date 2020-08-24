from web import app


class TestLogin:
    def test_login(self):
        app.LoginPage.login('standard_user', 'secret_sauce').login_succeed()

    def test_login_negative(self):
        app.LoginPage.login('test', 'test').login_failed()

    def test_login_logout(self):
        app.LoginPage.login('standard_user', 'secret_sauce').login_succeed()
        app.InventoryPage.open_menu()\
            .menu_should_be_opened()\
            .click_logout()
        app.LoginPage.should_be_opened()

