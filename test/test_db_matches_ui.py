from model.group import Group
from model.contact import Contacts
from timeit import timeit


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    # print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    # print(timeit(lambda: map(clean, db.get_group_list()), number=1))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
    # assert False

def test_contact_list(app, db):
    ui_contact_list = app.contact.get_contact_list()
    # print(timeit(lambda: app.contact.get_contact_list(), number=1))
    db_contact_list = db.get_contact_list()
    assert sorted(ui_contact_list, key=Group.id_or_max) == sorted(db_contact_list, key=Group.id_or_max)



