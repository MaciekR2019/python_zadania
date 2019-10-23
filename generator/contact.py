from model.contact import Contacts
import random
import string
import datetime
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


symbols = string.ascii_letters + string.digits + " " * 5
domains = ["hotmail.com", "gmail.com", "wp.pl", "tlen.pl", "yahoo.com", "onet.pl", "lol.pl"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
numbers = string.digits
letters = string.ascii_lowercase


def random_string(prefix, maxlen):
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).rstrip()


def random_numbers(prefix, maxlen):
    return prefix + "".join(random.choice(numbers) for i in range(maxlen))


def random_domain(domains):
    return random.choice(domains)


def random_letters():
    return "".join(random.choice(letters) for i in range(random.randrange(3, 10)))


def random_emails(prefix):
    return prefix + (random_letters() + '@' + random_domain(domains))


def random_www_site():
    return ('www.' + random_domain(domains))


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
             bday=random_month_day(), bmonth=random_month(months), byear=random_year(),
             aday=random_month_day(), amonth=random_month(months), ayear=current_year(), new_group="[none]",
             address2=random_string("address2", 50), phone2=random_numbers("phone2", 9),
             notes=random_string("notes", 30))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
