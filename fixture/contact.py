from selenium.webdriver.support.ui import Select
from model.contact import Contacts
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def otworz_strone_startowa(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def utworz(self, contacts):
        wd = self.app.wd
        self.przejdz_do_dodawania_kontaktow()
        self.wypelnij_kontakt(contacts)
        # Utworz kontakt
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.otworz_strone_startowa()
        self.contact_cache = None

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
        if text is not None:
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
        self.usun_kontakt_index(0)

    def usun_kontakt_index(self, index):
        wd = self.app.wd
        self.otworz_strone_startowa()
        self.wybierz_kontakt_index(index)
        # usuń pierwszy kontakt
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # potwierdzenie usuniecia w oknie dialogowym
        wd.switch_to.alert.accept()
        self.otworz_strone_startowa()
        self.contact_cache = None

    def usun_kontakt_id(self, id):
        wd = self.app.wd
        self.otworz_strone_startowa()
        self.wybierz_kontakt_id(id)
        # usuń pierwszy kontakt
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # potwierdzenie usuniecia w oknie dialogowym
        wd.switch_to.alert.accept()
        self.otworz_strone_startowa()
        self.contact_cache = None

    def wybierz_kontakt_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def wybierz_kontakt_id(self, id):
        wd = self.app.wd
        self.otworz_strone_startowa()
        wd.find_element_by_xpath("//tr[@name='entry']//input[@value='%s']" % id).click()


    def wybierz_pierwszy_kontakt(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edytuj_pierwszy_kontakt(self):
        self.edytuj_kontakt_index(0)

    def edytuj_kontakt_index(self, index, new_contact_data):
        wd = self.app.wd
        self.otworz_strone_startowa()
        self.wybierz_do_edycji_kontakt_index(index)
        self.wypelnij_kontakt(new_contact_data)
        # Zapisz zmianę
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def edytuj_kontakt_id(self, id, new_contact_data):
        wd = self.app.wd
        self.otworz_strone_startowa()
        self.wybierz_do_edycji_kontakt_id(id)
        self.wypelnij_kontakt(new_contact_data)
        # Zapisz zmianę
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def wybierz_do_edycji_kontakt_index(self, index):
        wd = self.app.wd
        self.otworz_strone_startowa()
        wiersz = wd.find_elements_by_name("entry")[index]
        td = wiersz.find_elements_by_tag_name("td")[7]
        td.find_element_by_tag_name("a").click()

    def wybierz_do_edycji_kontakt_id(self, id):
        wd = self.app.wd
        self.otworz_strone_startowa()
        wd.find_element_by_xpath("//a[contains(@href, 'edit.php?id=%s')]" % id).click()

    def wybierz_do_edycji_pierwszy_kontakt(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a//img[@title='Edit']").click()

    def wybierz_do_podgladu_kontakt_index(self, index):
        wd = self.app.wd
        self.otworz_strone_startowa()
        wiersz = wd.find_elements_by_name("entry")[index]
        td = wiersz.find_elements_by_tag_name("td")[6]
        td.find_element_by_tag_name("a").click()

    def wybierz_grupe_do_usuniecia_kontaktu(self, id):
        wd = self.app.wd
        #self.otworz_strone_startowa()
        wd.find_element_by_xpath("//select[@name='group']//option[@value='%s']" % id).click()


    def wybierz_grupe_dla_kontaktu_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='to_group']//option[@value='%s']" % id).click()
        # Potwierdź wybór przyciskiem
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        self.otworz_strone_startowa()

    def usun_kontakt_z_grupy(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='remove']").click()
        # powrót do grupy z której usunięto kontakt
        wd.find_element_by_xpath("//a[contains(@href, './?group=')]").click()

    def count(self):
        wd = self.app.wd
        self.otworz_strone_startowa()
        return len(wd.find_elements_by_name("selected[]"))


    def count_contacts_in_choosen_group(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def sprawdz_czy_istnieje(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("new_group")) > 0

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.otworz_strone_startowa()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                td = element.find_elements_by_tag_name("td")
                id = td[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = td[1].text
                firstname = td[2].text
                address = td[3].text
                all_emails = td[4].text
                all_phones = td[5].text
                self.contact_cache.append(Contacts(lastname=lastname, firstname=firstname, address=address, id=id,
                                                   all_emails_from_home_page=all_emails,
                                                   all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.wybierz_do_edycji_kontakt_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contacts(firstname=firstname, lastname=lastname, address=address, email=email, email2=email2,
                        email3=email3, id=id, home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.wybierz_do_podgladu_kontakt_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contacts(home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)
