# -*- coding: utf-8 -*-
from model.contact import Contacts


def test_dodaj_kontakt(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.utworz(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
