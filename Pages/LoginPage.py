from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.endpoint = ''

    USER_NAME = '#user-name'
    PASSWORD = '#password'
    BUTTON = '#login-button'
    DIV_SWAG = '.app_logo'

    def login(self, username, password):
        self.go_to_url()
        self.wait_for_selector_and_visible(self.USER_NAME)
        self.wait_for_selector_and_fill(self.USER_NAME, username)
        self.wait_for_selector_and_fill(self.PASSWORD, password)
        self.wait_for_selector_and_click(self.BUTTON)
        self.wait_for_selector_and_visible(self.DIV_SWAG)