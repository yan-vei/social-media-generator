# coding=utf-8

from sqlalchemy import Column, ForeignKey, Integer
from marshmallow import Schema, fields

from .entity import Base

class TextExtractsAndUsers(Base):
    __tablename__ = 'text_extracts_and_users'

    text_extract_id = Column(Integer, ForeignKey("text_extracts.id"), primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    def __init__(self, user_id, text_extract_id):
        self.user_id = user_id
        self.text_extract_id = text_extract_id


class TextExtractsAndUsersSchema(Schema):
    text_extract_id = fields.Number()
    user_id = fields.Number()