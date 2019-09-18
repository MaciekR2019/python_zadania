def test_usun_pierwszy_kontakt(app):
    app.session.zaloguj(username="admin", password="secret")
    app.contact.usun_pierwszy_kontakt()
    app.session.wyloguj()