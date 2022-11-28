from entities.user import User, UserSchema
from entities.entity import Session
import __main__ as main


def save_user(email, password, username):
    user = User(email, password, username)

    session = Session()

    session.add(user)
    session.commit()

    new_user = UserSchema().dump(user)
    session.close()

    return new_user


def already_exists(username, email):
    session = Session()
    if session.query(User).filter_by(username=username).first() or session.query(User).filter_by(email=email).first():
        return True
    return False


def login_user(username, password):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user and main.bcrypt.check_password_hash(user.password, password):
        session.close()
        return UserSchema().dump(user)
    session.close()
    return False


def get_user_by_token(token):
    session = Session()
    user = session.query(User).filter_by(token=str(token)).first()
    return UserSchema().dump(user)


def delete_users_batch():
    session = Session()
    session.query(User).delete()

    session.commit()
    session.close()


def get_all_users():
    session = Session()
    users = session.query(User).all()
    all_users = UserSchema(many=True).dump(users)
    session.close()
    return all_users