from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def wroc_na_strone_startowa(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def utworz(self, contacts):
        wd = self.app.wd
        self.przejdz_do_kontaktow()
        self.wypelnij_kontakt(contacts)
        # wybierz grupe
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]/option").click()
        # Utworz kontakt
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.wroc_na_strone_startowa()

    def wypelnij_kontakt(self, contacts):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacts.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contacts.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contacts.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contacts.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contacts.bday)
        wd.find_element_by_xpath("//div[@id='content']/form/select/option[13]").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contacts.bmonth)
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]/option[5]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contacts.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contacts.aday)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[15]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contacts.amonth)
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[9]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contacts.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contacts.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contacts.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contacts.notes)

    def przejdz_do_kontaktow(self):
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

    def edytuj_kontakt(self, contacts):
        wd = self.app.wd
        self.wroc_na_strone_startowa()
        # edytuj pierwszy kontakt
        wd.find_element_by_xpath("//a//img[@title='Edit']").click()
        self.wypelnij_kontakt(contacts)
        # Zapisz zmianę
        wd.find_element_by_xpath("//input[@value='Update']").click()
