# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contacts import Contacts

class TestDodajKontakt(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_dodaj_kontakt(self):
        wd = self.wd
        self.otworz_strone_startowa(wd)
        self.zaloguj(wd, username="admin", password="secret")
        self.przejdz_do_kontaktow(wd)
        self.utworz_kontakt(wd, Contacts(firstname="dfgdfg", middlename="dfg dfg dfg dg", lastname="fd gdf gdf gdf", nickname="dfg df gdfgdg", title="fgdf gdf gdfg dfgdfg d",
                            company="fdg dfg dfg dfg", address="fdg df gdf gdfg dfhfhjgh", home="fgh fgh fgh fgh", mobile="fg hfg hfg h",
                            work="fghfghfghfgjhjghj", fax="retrytui", email="hjkjhk jhkhjk hjk", email2="hjk hjk hjk hjkhjk", email3="hjk hjk hj",
                            homepage="fghfghfhgh fgh", bday="11", bmonth="April", byear="1995", aday="13", amonth="August", ayear="2005", address2="fgh fgh fhfg hf", phone2="hjkhjkhjkhjk",
                            notes="hjk hkhjkhjk hjkhjk hjk hj"))
        self.wroc_na_strone_startowa(wd)
        self.wyloguj(wd)

    def wyloguj(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def wroc_na_strone_startowa(self, wd):
        wd.find_element_by_link_text("home").click()

    def utworz_kontakt(self, wd, contacts):
        # Wypelnij kontakt
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
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]/option").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contacts.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contacts.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contacts.notes)
        # Utworz kontakt
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def przejdz_do_kontaktow(self, wd):
        wd.find_element_by_link_text("add new").click()

    def zaloguj(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def otworz_strone_startowa(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
