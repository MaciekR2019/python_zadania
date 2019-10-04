from model.contact import Contacts


def test_edytuj_pierwszy_kontakt(app):
    add_contact = Contacts(firstname="dfgdfg", middlename="dfg dfg dfg dg", lastname="fd gdf gdf gdf",
                       nickname="dfg df gdfgdg", title="fgdf gdf gdfg dfgdfg d",
                       company="fdg dfg dfg dfg", address="fdg df gdf gdfg dfhfhjgh",
                       home="fgh fgh fgh fgh", mobile="fg hfg hfg h",
                       work="fghfghfghfgjhjghj", fax="retrytui", email="hjkjhk jhkhjk hjk",
                       email2="hjk hjk hjk hjkhjk", email3="hjk hjk hj", homepage="fghfghfhgh fgh",
                       bday="11", bmonth="April", byear="1995", aday="13",
                       amonth="August", ayear="2005", new_group="[none]", address2="fgh fgh fhfg hf",
                       phone2="hjkhjkhjkhjk", notes="hjk hkhjkhjk hjkhjk hjk hj")
    if app.contact.count() == 0:
        app.contact.utworz(add_contact)
    old_contacts = app.contact.get_contact_list()
    edit_contact = Contacts(firstname="Zulu", middlename="Pierwszy", lastname="Gula")
    edit_contact.id = old_contacts[0].id
    app.contact.edytuj_pierwszy_kontakt(edit_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = edit_contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
