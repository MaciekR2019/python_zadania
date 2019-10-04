from model.group import Group
from random import randrange


def test_usun_losowa_grupe(app):
    group = Group(name="abc", header="123", footer="XYZ")
    if app.group.count() == 0:
        app.group.utworz(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.usun_grupe_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
