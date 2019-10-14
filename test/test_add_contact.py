# -*- coding: utf-8 -*-
from model.contact import Contacts
import pytest
from data.contacts import constant as testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_dodaj_kontakt(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.utworz(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
