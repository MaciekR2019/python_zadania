from model.group import Group


def test_usun_pierwsza_grupe(app):
    if app.group.count() == 0:
        app.group.utworz(Group(name="abc", header="123", footer="XYZ"))
    app.group.usun_pierwsza_grupe()
