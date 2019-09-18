from model.contact import Contacts


def test_edytuj_pierwszy_kontakt(app):
    app.session.zaloguj(username="admin", password="secret")
    app.contact.edytuj_pierwszy_kontakt(
        Contacts(firstname="edit_dfgdfg", middlename="edit_dfg dfg dfg dg", lastname="edit_fd gdf gdf gdf",
                 nickname="edit_dfg df gdfgdg",
                 title="edit_fgdf gdf gdfg dfgdfg d",
                 company="edit_fdg dfg dfg dfg", address="edit_fdg df gdf gdfg dfhfhjgh", home="edit_fgh fgh fgh fgh",
                 mobile="edit_fg hfg hfg h",
                 work="edit_fghfghfghfgjhjghj", fax="edit_retrytui", email="edit_hjkjhk jhkhjk hjk",
                 email2="edit_hjk hjk hjk hjkhjk",
                 email3="edit_hjk hjk hj",
                 homepage="edit_fghfghfhgh fgh", bday="11", bmonth="April", byear="1995", aday="13", amonth="August",
                 ayear="2005", address2="edit_fgh fgh fhfg hf", phone2="edit_hjkhjkhjkhjk",
                 notes="edit_hjk hkhjkhjk hjkhjk hjk hj"))
    app.session.wyloguj()
