from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def wroc_na_strone_startowa(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def utworz(self, contacts):
        wd = self.app.wd
        self.przejdz_do_dodawania_kontaktow()
        self.wypelnij_kontakt(contacts)
        # Utworz kontakt
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.wroc_na_strone_startowa()

    def wypelnij_kontakt(self, contacts):
        self.zmien_wartosc_pola("firstname", contacts.firstname)
        self.zmien_wartosc_pola("middlename", contacts.middlename)
        self.zmien_wartosc_pola("lastname", contacts.lastname)
        self.zmien_wartosc_pola("nickname", contacts.nickname)
        self.zmien_wartosc_pola("title", contacts.title)
        self.zmien_wartosc_pola("company", contacts.company)
        self.zmien_wartosc_pola("address", contacts.address)
        self.zmien_wartosc_pola("home", contacts.home)
        self.zmien_wartosc_pola("mobile", contacts.mobile)
        self.zmien_wartosc_pola("work", contacts.work)
        self.zmien_wartosc_pola("fax", contacts.fax)
        self.zmien_wartosc_pola("email", contacts.email)
        self.zmien_wartosc_pola("email2", contacts.email2)
        self.zmien_wartosc_pola("email3", contacts.email3)
        self.zmien_wartosc_pola("homepage", contacts.homepage)
        self.wybierz_z_listy("bday", contacts.bday, "//div[@id='content']/form/select[1]/option[13]")
        self.wybierz_z_listy("bmonth", contacts.bmonth, "//div[@id='content']/form/select[2]/option[5]")
        self.zmien_wartosc_pola("byear", contacts.byear)
        self.wybierz_z_listy("aday", contacts.aday, "//div[@id='content']/form/select[3]/option[15]")
        self.wybierz_z_listy("amonth", contacts.amonth, "//div[@id='content']/form/select[4]/option[9]")
        self.zmien_wartosc_pola("ayear", contacts.ayear)
        # jeśli pole grupy istnieje to wypełnia
        if self.sprawdz_czy_istnieje():
            self.wybierz_z_listy("new_group", contacts.new_group, "//div[@id='content']/form/select[5]/option[1]")
        else:
            print("Formualrz edycji kontaktów nie zawiera pola grupy")
        self.zmien_wartosc_pola("address2", contacts.address2)
        self.zmien_wartosc_pola("phone2", contacts.phone2)
        self.zmien_wartosc_pola("notes", contacts.notes)

    def wybierz_z_listy(self, field_name, text, xpath):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
        wd.find_element_by_xpath(xpath).click()

    def zmien_wartosc_pola(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def przejdz_do_dodawania_kontaktow(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def usun_pierwszy_kontakt(self):
        wd = self.app.wd
        self.wroc_na_strone_startowa()
        # wybierz pierwszy kontakt
        wd.find_element_by_name("selected[]").click()
        # usuń pierwszy kontakt
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # potwierdzenie usuniecia w oknie dialogowym
        wd.switch_to.alert.accept()
        self.wroc_na_strone_startowa()

    def edytuj_pierwszy_kontakt(self, new_contact_data):
        wd = self.app.wd
        self.wroc_na_strone_startowa()
        # edytuj pierwszy kontakt
        wd.find_element_by_xpath("//a//img[@title='Edit']").click()
        self.wypelnij_kontakt(new_contact_data)
        # Zapisz zmianę
        wd.find_element_by_xpath("//input[@value='Update']").click()

    def count(self):
        wd = self.app.wd
        self.wroc_na_strone_startowa()
        return len(wd.find_elements_by_name("selected[]"))

    def sprawdz_czy_istnieje(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("new_group")) > 0
