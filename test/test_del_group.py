from model.group import Group


def test_usun_pierwsza_grupe(app):
    group = Group(name="abc", header="123", footer="XYZ")
    if app.group.count() == 0:
        app.group.utworz(group)
    old_groups = app.group.get_group_list()
    app.group.usun_pierwsza_grupe()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
