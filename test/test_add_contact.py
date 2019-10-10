# -*- coding: utf-8 -*-
from model.contact import Contacts
import pytest
import random
import string
import datetime

symbols = string.ascii_letters + string.digits
domains = ["hotmail.com", "gmail.com", "wp.pl", "tlen.pl", "yahoo.com", "onet.pl", "lol.pl"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
numbers = string.digits
letters = string.ascii_lowercase


def random_string(prefix, maxlen):
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(prefix, maxlen):
    return prefix + "".join(random.choice(numbers) for i in range(maxlen))


def random_domain(domains):
    return random.choice(domains)


def random_letters():
    return "".join(random.choice(letters) for i in range(random.randrange(10)))


def random_emails(prefix):
    return prefix + (random_letters() + '@' + random_domain(domains))


def random_www_site():
    return ('www' + random_domain(domains))


def random_month(months):
    return random.choice(months)


def current_year():
    now = datetime.datetime.now()
    return now.year


def random_year():
    return (current_year() - random.randint(20, 50))


def random_month_day():
    day = random.randint(1, 30)
    return str(day)


testdata = [
    Contacts(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
             lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
             title=random_string("title", 20), company=random_string("company", 20),
             address=random_string("address", 50), home=random_numbers("home", 9), mobile=random_numbers("mobile", 9),
             work=random_numbers("work", 9), fax=random_numbers("fax", 9), email=random_emails("email"),
             email2=random_emails("email2"), email3=random_emails("email3"), homepage=random_www_site(),
             bday=("" + random_month_day() + ""), bmonth=random_month(months), byear=random_year(),
             aday=("" + random_month_day() + ""), amonth=random_month(months), ayear=current_year(), new_group="[none]",
             address2=random_string("address2", 50), phone2=random_numbers("phone2", 9),
             notes=random_string("notes", 30))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_dodaj_kontakt(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.utworz(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
