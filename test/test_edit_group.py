from model.group import Group


def test_edytuj_pierwsza_grupe_name(app):
    app.group.edytuj_pierwsza_grupe(Group(name="New name"))


def test_edytuj_pierwsza_grupe_header(app):
    app.group.edytuj_pierwsza_grupe(Group(header="New header"))


def test_edytuj_pierwsza_grupe_footer(app):
    app.group.edytuj_pierwsza_grupe(Group(footer="New footer"))
