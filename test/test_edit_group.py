from model.group import Group
import random
import string

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    chars = "".join([random.choice(symbols) for i in range(random.randrange(5,maxlen))]).strip()
    return chars

def test_edytuj_losowa_grupe_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.utworz(Group(name=random_string(30), header=random_string(60), footer=random_string(60)))
    old_groups = db.get_group_list()
    chosen_group = random.choice(old_groups)
    app.group.edytuj_grupe_id(chosen_group.id, Group(name=random_string(30), header=random_string(60), footer=random_string(60)))
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert len(old_groups) == len(app.group.get_group_list())

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
