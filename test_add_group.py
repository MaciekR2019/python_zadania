# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_dodaj_grupe(app):
    app.zaloguj(username="admin", password="secret")
    app.utworz_grupe(Group(name="grupa1", header="jakiś tekst", footer="jakiś tekstsdsdsd"))
    app.wyloguj()


def test_dodaj_pusta_grupe(app):
    app.zaloguj(username="admin", password="secret")
    app.utworz_grupe(Group(name="", header="", footer=""))
    app.wyloguj()
