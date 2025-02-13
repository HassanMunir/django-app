def test_create_user(db_session):
    from myapp.models import User

    db_session.query(User).filter_by(email="admin@admin.com").delete()
    db_session.commit()

    new_user = User(name="admin", email="admin@admin.com")
    db_session.add(new_user)
    db_session.commit()

    user = db_session.query(User).filter_by(email="admin@admin.com").first()

    assert user is not None
    assert user.name == "admin"
    assert user.email == "admin@admin.com"
