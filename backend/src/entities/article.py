# coding=utf-8

from sqlalchemy import Column, String, DateTime

from marshmallow import Schema, fields

from .entity import Entity, Base


class Article(Entity, Base):
    __tablename__ = 'articles'

    text = Column(String)
    url = Column(String)
    title = Column(String)

    def __init__(self, text, url, title, added_by):
        Entity.__init__(self, added_by)
        self.text = text
        self.url = url
        self.title = title

class ArticleSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    text = fields.Str()
    url = fields.Str()

