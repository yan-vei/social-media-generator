# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey

from marshmallow import Schema, fields

from .entity import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    post = Column(String)
    score = Column(Integer)
    notes = Column(String)
    length = Column(Integer)
    template = Column(String)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=True)
    text_extract_id = Column(Integer, ForeignKey("text_extracts.id"), nullable=True)

    def __init__(self, post, score, length, notes, template, article_id, text_extract_id):
        self.article_id = article_id
        self.text_extract_id = text_extract_id
        self.post = post
        self.score = score
        self.length = length
        self.notes = notes
        self.template = template

class PostSchema(Schema):
    id = fields.Number()
    score = fields.Number()
    length = fields.Number()
    notes = fields.Str()
    template = fields.Str()
    article_id = fields.Number(allow_none=True)
    text_extract_id = fields.Number(allow_none=True)
    post = fields.Str()
    created_at = fields.Str()
