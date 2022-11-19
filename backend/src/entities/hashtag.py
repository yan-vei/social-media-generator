# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey, Float

from marshmallow import Schema, fields

from .entity import Base


class Hashtag(Base):
    __tablename__ = 'hashtags'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=True)
    text_extract_id = Column(Integer, ForeignKey("text_extracts.id"), nullable=True)
    hashtag = Column(String)
    score = Column(Float)

    def __init__(self, article_id, text_extract_id, hashtag, score):
        self.article_id = article_id
        self.text_extract_id = text_extract_id
        self.hashtag = hashtag
        self.score = score


class HashtagSchema(Schema):
    id = fields.Number()
    article_id = fields.Number()
    hashtag = fields.Str()
    score = fields.Float()
    article_id = fields.Number(allow_none=True)
    text_extract_id = fields.Number(allow_none=True)