from model.group import Group


def test_edytuj_pierwsza_grupe_name(app):
    if app.group.count() == 0:
        app.group.utworz(Group(name="a1b2c3", header="1-2-3", footer="X-Y-Z"))
    app.group.edytuj_pierwsza_grupe(Group(name="New name"))


def test_edytuj_pierwsza_grupe_header(app):
    if app.group.count() == 0:
        app.group.utworz(Group(name="a1b2c3", header="1-2-3", footer="X-Y-Z"))
    app.group.edytuj_pierwsza_grupe(Group(header="New header"))


def test_edytuj_pierwsza_grupe_footer(app):
    if app.group.count() == 0:
        app.group.utworz(Group(name="a1b2c3", header="1-2-3", footer="X-Y-Z"))
    app.group.edytuj_pierwsza_grupe(Group(footer="New footer"))
