# coding=utf-8

from sqlalchemy import Column, String
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from .entity import Base
from .text_entity import TextEntity


class Article(TextEntity, Base):
    __tablename__ = 'articles'

    text = Column(String)
    url = Column(String)
    title = Column(String)
    added_by = Column(String)

    posts = relationship("Post", backref="articles")

    def __init__(self, text, url, title, added_by):
        TextEntity.__init__(self)
        self.text = text
        self.url = url
        self.title = title
        self.added_by = added_by

class ArticleSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    text = fields.Str()
    url = fields.Str()
    added_by = fields.Str()
    added_at = fields.Str()

