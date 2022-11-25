from entities.user import User, UserSchema
from entities.entity import Session
from main import bcrypt


def save_user(email, password, username):
    user = User(email, password, username)

    session = Session()

    try:
        session.add(user)
        session.commit()
    except:
        return "Already exists"

    new_user = UserSchema().dump(user)
    session.close()

    return new_user


def login_user(username, password):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return UserSchema().dump(user)
    return False


def get_user_by_token(token):
    session = Session()
    user = session.query(User).filter_by(token=token).first()
    return UserSchema().dump(user)


def delete_users_batch():
    session = Session()
    session.query(User).delete()

    session.commit()
    session.close()