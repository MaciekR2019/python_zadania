from model.contact import Contacts
from model.group import Group
import random

def test_dodaj_kontakt_do_grupy(app, db):
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
    all_contacts = db.get_contact_list()
    chosen_contact = random.choice(all_contacts)
    app.contact.wybierz_kontakt_id(chosen_contact.id)
    all_groups = db.get_group_list()
    chosen_group = random.choice(all_groups)
    old_contacts_in_group = db.get_contacts_in_group()
    app.contact.wybierz_grupe_dla_kontaktu_id(chosen_group.id)
    new_contacts_in_group = db.get_contacts_in_group()
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    print("\nWybrany kontakt:", chosen_contact)
    print("\nWybrana grupa:", chosen_group)
    print("Przed dodaniem:", len(old_contacts_in_group))
    print("Po dodaniu:",len(new_contacts_in_group))
