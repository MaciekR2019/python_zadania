# -*- coding: utf-8 -*-
from model.group import Group


def test_dodaj_grupe(app):
    app.group.utworz(Group(name="grupa1", header="jakiś tekst", footer="jakiś tekstsdsdsd"))


def test_dodaj_pusta_grupe(app):
    app.group.utworz(Group(name="", header="", footer=""))
