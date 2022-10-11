# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey

from marshmallow import Schema, fields

from .entity import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    post = Column(String)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=True)
    text_extract_id = Column(Integer, ForeignKey("text_extracts.id"), nullable=True)

    def __init__(self, post, article_id, text_extract_id):
        self.article_id = article_id
        self.text_extract_id = text_extract_id
        self.post = post

class PostSchema(Schema):
    id = fields.Number()
    article_id = fields.Number(allow_none=True)
    text_extract_id = fields.Number(allow_none=True)
    post = fields.Str()
    created_at = fields.Str()
