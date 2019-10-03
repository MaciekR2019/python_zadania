# -*- coding: utf-8 -*-
from model.contact import Contacts


def test_dodaj_kontakt(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contacts(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                       title="title",
                       company="company", address="address", home="home",
                       mobile="mobile",
                       work="work", fax="fax", email="email", email2="email2",
                       email3="email3",
                       homepage="homepage", bday="11", bmonth="April", byear="1995", aday="13", amonth="August",
                       ayear="2005", new_group="[none]", address2="address2", phone2="phone2",
                       notes="notes")
    app.contact.utworz(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
