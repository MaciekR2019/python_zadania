from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def wyloguj(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def powrot_do_grup(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def utworz_grupe(self, group):
        wd = self.wd
        self.przejdz_do_grup()
        # Dodaj grupe
        wd.find_element_by_name("new").click()
        # Wypelnij grupe
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Zapisz grupe
        wd.find_element_by_name("submit").click()
        self.powrot_do_grup()

    def przejdz_do_grup(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def zaloguj(self, username, password):
        wd = self.wd
        self.otworz_strone_startowa()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def otworz_strone_startowa(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()