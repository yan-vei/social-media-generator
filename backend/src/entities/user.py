# coding=utf-8

from sqlalchemy import Column, String, Integer, DateTime, Boolean, UniqueConstraint
from marshmallow import Schema, fields
from .entity import Base
from main import bcrypt
from sqlalchemy.orm import relationship
import datetime
import secrets

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_on = Column(DateTime, nullable=False)
    admin = Column(Boolean, nullable=False, default=False)

    articles = relationship("Article", backref="users")
    text_extracts = relationship("TextExtract", backref="users")
    articles = relationship("Article", backref="articles_and_users")
    text_extracts = relationship("TextExtract", backref="text_extracts_and_users")

    def __init__(self, email, password, username, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.username = username
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        self.token = secrets.token_hex(32)


class UserSchema(Schema):
    id = fields.Number()
    email = fields.Str()
    password = fields.Str()
    username = fields.Str()
    registered_on = fields.DateTime()
    admin = fields.Boolean()
    token = fields.Str()
