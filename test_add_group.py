# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class TestDodajGrupe(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_dodaj_grupe(self):
        wd = self.wd
        self.otworz_strone_startowa(wd)
        self.zaloguj(wd, username="admin", password="secret")
        self.przejdz_do_grup(wd)
        self.utworz_grupe(wd, Group(name="grupa1", header="jakiś tekst", footer="jakiś tekstsdsdsd"))
        self.powrot_do_grup(wd)
        self.wyloguj(wd)

    def test_dodaj_pusta_grupe(self):
        wd = self.wd
        self.otworz_strone_startowa(wd)
        self.zaloguj(wd, username="admin", password="secret")
        self.przejdz_do_grup(wd)
        self.utworz_grupe(wd, Group(name="", header="", footer=""))
        self.powrot_do_grup(wd)
        self.wyloguj(wd)

    def wyloguj(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def powrot_do_grup(self, wd):
        wd.find_element_by_link_text("groups").click()

    def utworz_grupe(self, wd, group):
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

    def przejdz_do_grup(self, wd):
        wd.find_element_by_link_text("groups").click()

    def zaloguj(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
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