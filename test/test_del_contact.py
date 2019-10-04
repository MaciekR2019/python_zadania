from model.contact import Contacts


def test_usun_pierwszy_kontakt(app):
    contact = Contacts(firstname="dfgdfg", middlename="dfg dfg dfg dg", lastname="fd gdf gdf gdf",
                       nickname="dfg df gdfgdg", title="fgdf gdf gdfg dfgdfg d",
                       company="fdg dfg dfg dfg", address="fdg df gdf gdfg dfhfhjgh",
                       home="fgh fgh fgh fgh", mobile="fg hfg hfg h", work="fghfghfghfgjhjghj",
                       fax="retrytui", email="hjkjhk jhkhjk hjk", email2="hjk hjk hjk hjkhjk",
                       email3="hjk hjk hj", homepage="fghfghfhgh fgh", bday="11", bmonth="April",
                       byear="1995", aday="13", amonth="August", ayear="2005", new_group="[none]",
                       address2="fgh fgh fhfg hf", phone2="hjkhjkhjkhjk",
                       notes="hjk hkhjkhjk hjkhjk hjk hj")
    if app.contact.count() == 0:
        app.contact.utworz(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.usun_pierwszy_kontakt()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
