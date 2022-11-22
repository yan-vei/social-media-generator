# coding=utf-8

from sqlalchemy import Column, String, ForeignKey, Integer
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from .entity import Base
from .text_entity import TextEntity


class TextExtract(TextEntity, Base):
    __tablename__ = 'text_extracts'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    title = Column(String)
    added_by = Column(Integer, ForeignKey("users.id"))

    posts = relationship("Post", backref="text_extracts")
    users = relationship("TextExtractsAndUsers", backref="text_extracts_and_users")

    def __init__(self, text, title, added_by):
        TextEntity.__init__(self)
        self.text = text
        self.title = title
        self.added_by = added_by


class TextExtractSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    text = fields.Str()
    added_by = fields.Number()
    added_at = fields.Str()