# -*- coding: utf-8 -*-
from model.group import Group


def test_dodaj_grupe(app):
    app.session.zaloguj(username="admin", password="secret")
    app.group.utworz(Group(name="grupa1", header="jakiś tekst", footer="jakiś tekstsdsdsd"))
    app.session.wyloguj()


def test_dodaj_pusta_grupe(app):
    app.session.zaloguj(username="admin", password="secret")
    app.group.utworz(Group(name="", header="", footer=""))
    app.session.wyloguj()
