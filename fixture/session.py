class SessionHelper:

    def __init__(self, app):
        self.app = app

    def zaloguj(self, username, password):
        wd = self.app.wd
        self.app.otworz_strone_startowa()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def wyloguj(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

