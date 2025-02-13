import pytest
from myapp.models import User


@pytest.mark.django_db
def test_user_creation(db_session):
    user = User(name="admin", email="admin@admin.com")
    db_session.add(user)
    db_session.commit()

    saved_user = db_session.query(User).filter_by(email="admin@admin.com").first()
    assert saved_user is not None
    assert saved_user.name == "admin"


@pytest.mark.django_db
def test_user_email_uniqueness(db_session):
    user1 = User(name="user1", email="user1@admin.com")
    db_session.add(user1)
    db_session.commit()

    user2 = User(name="user2", email="user1@admin.com")
    db_session.add(user2)

    with pytest.raises(Exception, match="UNIQUE constraint failed: users.email"):
        db_session.commit()


@pytest.mark.django_db
def test_user_name_validation(db_session):
    invalid_user = User(name="", email="invalid@admin.com")
    db_session.add(invalid_user)

    with pytest.raises(Exception, match="Name cannot be empty."):
        db_session.commit()
