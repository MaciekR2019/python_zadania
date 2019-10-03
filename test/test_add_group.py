# -*- coding: utf-8 -*-
from model.group import Group


def test_dodaj_grupe(app):
    old_groups = app.group.get_group_list()
    group = Group(name="grupa1", header="jakiś tekst", footer="jakiś tekstsdsdsd")
    app.group.utworz(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_dodaj_pusta_grupe(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.utworz(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
