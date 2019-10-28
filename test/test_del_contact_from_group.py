from model.contact import Contacts
from model.group import Group
import random
from random import randrange


def test_usun_kontakt_z_grupy(app, db):
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
        print("\nDodano kontakt")
    if len(db.get_group_list()) == 0:
        app.group.utworz(Group(name="abc"))
        print("\nDodano grupę")
    if len(db.get_contacts_in_group()) == 0:
        # wybranie kontaktu bez grupy i dodanie do grupy
        contacts = db.get_contacts_not_in_group()
        contact = random.choice(contacts)
        app.contact.wybierz_kontakt_id(contact.id)
        groups = db.get_group_list()
        group = random.choice(groups)
        app.contact.wybierz_grupe_dla_kontaktu_id(group.id)
        print("\nDodano kontakt do grupy")
    # wybieram grupę z kontaktami
    all_groups = db.get_contacts_in_group()
    chosen_group = random.choice(all_groups)
    app.contact.wybierz_grupe_do_usuniecia_kontaktu(chosen_group.id)
    all_contacts_in_group = db.get_contacts_in_group()
    index = randrange(app.contact.count_contacts_in_choosen_group())
    app.contact.wybierz_kontakt_index(index)
    app.contact.usun_kontakt_z_grupy()
    print("\nUsunięto kontakt z grupy")
    new_contacts_in_group = db.get_contacts_in_group()
    assert len(all_contacts_in_group) - 1 == len(new_contacts_in_group)

