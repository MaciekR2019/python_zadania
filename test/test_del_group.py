def test_usun_pierwsza_grupe(app):
    app.session.zaloguj(username="admin", password="secret")
    app.group.usun_pierwsza_grupe()
    app.session.wyloguj()
