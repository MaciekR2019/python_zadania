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
        self.wypelnij_grupe(group)
        # Zapisz grupe
        wd.find_element_by_name("submit").click()
        self.powrot_do_grup()

    def wypelnij_grupe(self, group):
        # wd = self.app.wd
        self.zmien_wartosc_pola("group_name", group.name)
        self.zmien_wartosc_pola("group_header", group.header)
        self.zmien_wartosc_pola("group_footer", group.footer)

    def zmien_wartosc_pola(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def usun_pierwsza_grupe(self):
        wd = self.app.wd
        self.przejdz_do_grup()
        # wybierz pierwszą grupę
        wd.find_element_by_name("selected[]").click()
        # usuń pierwszą grupę
        wd.find_element_by_name("delete").click()
        self.powrot_do_grup()

    def przejdz_do_grup(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def wybierz_pierwsza_grupe(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edytuj_pierwsza_grupe(self, new_group_data):
        wd = self.app.wd
        self.przejdz_do_grup()
        self.wybierz_pierwsza_grupe()
        # kliknij edytuj
        wd.find_element_by_xpath("//input[@value='Edit group']").click()
        self.wypelnij_grupe(new_group_data)
        # zapisz zmianę
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.powrot_do_grup()
