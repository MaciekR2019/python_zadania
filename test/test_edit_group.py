from model.group import Group
from random import randrange


def test_edytuj_losowa_grupe_name(app):
    if app.group.count() == 0:
        app.group.utworz(Group(name="a1b2c3", header="1-2-3", footer="X-Y-Z"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New name")
    group.id = old_groups[index].id
    app.group.edytuj_grupe_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edytuj_pierwsza_grupe_header(app):
#     if app.group.count() == 0:
#         app.group.utworz(Group(name="a1b2c3", header="1-2-3", footer="X-Y-Z"))
#     old_groups = app.group.get_group_list()
#     app.group.edytuj_pierwsza_grupe(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edytuj_pierwsza_grupe_footer(app):
#     if app.group.count() == 0:
#         app.group.utworz(Group(name="a1b2c3", header="1-2-3", footer="X-Y-Z"))
#     old_groups = app.group.get_group_list()
#     app.group.edytuj_pierwsza_grupe(Group(footer="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
