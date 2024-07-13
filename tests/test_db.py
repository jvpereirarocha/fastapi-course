from sqlalchemy import select

from fast_course.models.users import User


def test_create_user(session):
    new_user = User(username='joao', password='mypass@123', email='joao@gmail.com')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'joao'))

    assert user.username == 'joao'
    assert user.email == 'joao@gmail.com'
