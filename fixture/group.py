class GroupHelper:

    def __init__(self, app):
        self.app = app


    def powrot_do_grup(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def utworz(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
