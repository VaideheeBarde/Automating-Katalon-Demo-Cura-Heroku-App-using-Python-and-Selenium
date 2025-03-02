class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = "txt-username"
        self.password_field = "txt-password"
        self.login_button = "btn-login"

    def enter_username(self, username):
        self.driver.find_element("id", self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("id", self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element("id", self.login_button).click()
