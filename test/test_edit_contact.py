from model.contact import Contacts


def test_edytuj_pierwszy_kontakt(app):
    if app.contact.count() == 0:
        app.contact.utworz(Contacts(firstname="dfgdfg", middlename="dfg dfg dfg dg", lastname="fd gdf gdf gdf",
                                    nickname="dfg df gdfgdg", title="fgdf gdf gdfg dfgdfg d",
                                    company="fdg dfg dfg dfg", address="fdg df gdf gdfg dfhfhjgh",
                                    home="fgh fgh fgh fgh", mobile="fg hfg hfg h",
                                    work="fghfghfghfgjhjghj", fax="retrytui", email="hjkjhk jhkhjk hjk",
                                    email2="hjk hjk hjk hjkhjk", email3="hjk hjk hj", homepage="fghfghfhgh fgh",
                                    bday="11", bmonth="April", byear="1995", aday="13",
                                    amonth="August", ayear="2005", new_group="[none]", address2="fgh fgh fhfg hf",
                                    phone2="hjkhjkhjkhjk", notes="hjk hkhjkhjk hjkhjk hjk hj"))
    app.contact.edytuj_pierwszy_kontakt(
        Contacts(firstname="New firstname", middlename="New middlename", lastname="New lastname",
                 nickname="New nickname", title="New title", company="New company", address="", home="", mobile="",
                 work="", fax="", email="", email2="", email3="", homepage="", bday="12", bmonth="May", byear="1990",
                 aday="10", amonth="August", ayear="2000", new_group="[none]", address2="", phone2="", notes=""))
