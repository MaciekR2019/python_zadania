from model.contact import Contacts
import random


def test_edytuj_losowy_kontakt(app, db, check_ui):
    add_contact = Contacts(firstname="dfgdfg", middlename="dfg dfg dfg dg", lastname="fd gdf gdf gdf",
                           nickname="dfg df gdfgdg", title="fgdf gdf gdfg dfgdfg d",
                           company="fdg dfg dfg dfg", address="fdg df gdf gdfg dfhfhjgh",
                           home="fgh fgh fgh fgh", mobile="fg hfg hfg h",
                           work="fghfghfghfgjhjghj", fax="retrytui", email="hjkjhk jhkhjk hjk",
                           email2="hjk hjk hjk hjkhjk", email3="hjk hjk hj", homepage="fghfghfhgh fgh",
                           bday="11", bmonth="April", byear="1995", aday="13",
                           amonth="August", ayear="2005", new_group="[none]", address2="fgh fgh fhfg hf",
                           phone2="hjkhjkhjkhjk", notes="hjk hkhjkhjk hjkhjk hjk hj")
    if len(db.get_contact_list()) == 0:
        app.contact.utworz(add_contact)
    old_contacts = db.get_contact_list()
    chosen_contact = random.choice(old_contacts)
    edit_contact = Contacts(firstname="Zulu", middlename="Pierwszy", lastname="Gula")
    app.contact.edytuj_kontakt_id(chosen_contact.id, edit_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(app.contact.get_contact_list(), key=Contacts.id_or_max)
