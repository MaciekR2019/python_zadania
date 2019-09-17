# -*- coding: utf-8 -*-

from model.contact import Contacts


def test_dodaj_kontakt(app):
    app.session.zaloguj(username="admin", password="secret")
    app.contact.utworz(
        Contacts(firstname="dfgdfg", middlename="dfg dfg dfg dg", lastname="fd gdf gdf gdf", nickname="dfg df gdfgdg",
                 title="fgdf gdf gdfg dfgdfg d",
                 company="fdg dfg dfg dfg", address="fdg df gdf gdfg dfhfhjgh", home="fgh fgh fgh fgh",
                 mobile="fg hfg hfg h",
                 work="fghfghfghfgjhjghj", fax="retrytui", email="hjkjhk jhkhjk hjk", email2="hjk hjk hjk hjkhjk",
                 email3="hjk hjk hj",
                 homepage="fghfghfhgh fgh", bday="11", bmonth="April", byear="1995", aday="13", amonth="August",
                 ayear="2005", address2="fgh fgh fhfg hf", phone2="hjkhjkhjkhjk",
                 notes="hjk hkhjkhjk hjkhjk hjk hj"))
    app.session.wyloguj()
