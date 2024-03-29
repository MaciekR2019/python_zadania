from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def przejdz_do_grup(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    group_cache = None

    def utworz(self, group):
        wd = self.app.wd
        self.przejdz_do_grup()
        # Dodaj grupe
        wd.find_element_by_name("new").click()
        self.wypelnij_grupe(group)
        # Zapisz grupe
        wd.find_element_by_name("submit").click()
        self.przejdz_do_grup()
        self.group_cache = None

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

    def usun_grupe_index(self, index):
        wd = self.app.wd
        self.przejdz_do_grup()
        self.wybierz_grupe_index(index)
        # usuń pierwszą grupę
        wd.find_element_by_name("delete").click()
        self.przejdz_do_grup()
        self.group_cache = None

    def usun_grupe_id(self, id):
        wd = self.app.wd
        self.przejdz_do_grup()
        self.wybierz_grupe_id(id)
        # usuń pierwszą grupę
        wd.find_element_by_name("delete").click()
        self.przejdz_do_grup()
        self.group_cache = None

    def usun_pierwsza_grupe(self):
        self.usun_grupe_index(0)

    def wybierz_grupe_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def wybierz_grupe_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def wybierz_pierwsza_grupe(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edytuj_pierwsza_grupe(self):
        self.edytuj_grupe_index(0)

    def edytuj_grupe_index(self, index, new_group_data):
        wd = self.app.wd
        self.przejdz_do_grup()
        self.wybierz_grupe_index(index)
        # kliknij edytuj
        wd.find_element_by_xpath("//input[@value='Edit group']").click()
        self.wypelnij_grupe(new_group_data)
        # zapisz zmianę
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.przejdz_do_grup()
        self.group_cache = None

    def edytuj_grupe_id(self, id, new_group_data):
        wd = self.app.wd
        self.przejdz_do_grup()
        self.wybierz_grupe_id(id)
        # kliknij edytuj
        wd.find_element_by_xpath("//input[@value='Edit group']").click()
        self.wypelnij_grupe(new_group_data)
        # zapisz zmianę
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.przejdz_do_grup()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.przejdz_do_grup()
        return len(wd.find_elements_by_name("selected[]"))


    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.przejdz_do_grup()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
