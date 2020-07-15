from web import app


class TestLogin:
    def test_login(self):
        app.LoginPage.login('standard_user', 'secret_sauce').login_succeed()

    def test_login_negative(self):
        app.LoginPage.login('test', 'test').login_failed()

