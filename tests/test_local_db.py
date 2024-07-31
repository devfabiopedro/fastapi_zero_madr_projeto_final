from sqlalchemy import select

from madr.models import Account


def test_create_user(session):
    new_user = Account(
        username='fabio', email='fabio@email.com', password='fabiopass'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(Account).where(Account.username == 'fabio'))

    assert user.username == 'fabio'
