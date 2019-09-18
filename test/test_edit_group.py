from model.group import Group


def test_edytuj_pierwsza_grupe(app):
    app.session.zaloguj(username="admin", password="secret")
    app.group.edytuj_pierwsza_grupe(
        Group(name="edit_grupa1", header="edit_jakiś tekst", footer="edit_jakiś tekstsdsdsd"))
    app.session.wyloguj()
