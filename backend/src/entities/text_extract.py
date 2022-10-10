# coding=utf-8

from sqlalchemy import Column, String

from marshmallow import Schema, fields

from .text_entity import TextEntity, Base


class TextExtract(TextEntity, Base):
    __tablename__ = 'text_extracts'

    text = Column(String)
    title = Column(String)

    def __init__(self, text, title, added_by):
        TextEntity.__init__(self)
        self.text = text
        self.title = title
        self.added_by = added_by


class TextExtractSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    text = fields.Str()
    added_by = fields.Str()
    added_at = fields.Str()