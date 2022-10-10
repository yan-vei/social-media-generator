# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey

from marshmallow import Schema, fields

from .text_entity import Base


class Post(Base):
    __tablename__ = 'posts'

    post = Column(String)
    article_id = Column(Integer, ForeignKey("articles.id"))
    text_extract_id = Column(Integer, ForeignKey("text_extracts.id"))

    def __init__(self, post, article_id, text_extract_id):
        self.article_id = article_id
        self.text_extract_id = text_extract_id
        self.post = post


class PostSchema(Schema):
    id = fields.Number()
    article_id = fields.Number()
    text_extract_id = fields.Number()
    post = fields.Str()
    created_at = fields.Str()