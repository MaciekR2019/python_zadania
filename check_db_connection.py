from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contacts

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # l = db.get_contacts_not_in_group(Group(id="268"))
    # for item in l:
    #     print(item)
    # print(len(l))
    l = db.get_contacts_in_group(Group(id="331"))
    #l = db.get_contacts_not_in_group(Contacts())
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
