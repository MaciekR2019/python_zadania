import re
from random import randrange
from model.contact import Contacts


def test_all_contacts_on_home_page_vs_db(app, db):
    list_range = len(db.get_contact_list())
    for row in range(list_range):
        contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contacts.id_or_max)[row]
        contact_from_db = sorted(db.get_contact_list(), key=Contacts.id_or_max)[row]
        assert sorted(contact_from_db.lastname) == sorted(contact_from_home_page.lastname)
        assert sorted(contact_from_db.firstname) == sorted(contact_from_home_page.firstname)
        assert sorted(address_clean(contact_from_db.address)) == sorted(contact_from_home_page.address)
        assert sorted(merge_phones_like_on_home_page(contact_from_db)) == sorted(
            contact_from_home_page.all_phones_from_home_page)
        assert sorted(merge_emails_like_on_home_page(contact_from_db)) == sorted(
            contact_from_home_page.all_emails_from_home_page)



def test_phones_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert sorted(contact_from_home_page.all_phones_from_home_page) == sorted(
        merge_phones_like_on_home_page(contact_from_edit_page))


def test_phones_on_view_page(app):
    index = randrange(app.contact.count())
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_address_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == address_clean(contact_from_edit_page.address)


def test_names_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


def test_emails_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert check_email(contact_from_home_page.all_emails_from_home_page) == check_email(
        merge_emails_like_on_home_page(contact_from_edit_page))


def clear(s):
    return re.sub("[() -]", "", s)


def address_clean(s):
    return re.sub("  ", " ", s)


regex = r"[^@]+@[^@]+.[^@]+"


def check_email(email):
    if re.search(regex, email):
        print("Adres email poprawny")
    else:
        print("Błędny adres email", "\n", (email), "\n")


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.work, contact.mobile, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))
