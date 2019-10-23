# -*- coding: utf-8 -*-
from model.group import Group


def test_dodaj_grupe(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.utworz(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
