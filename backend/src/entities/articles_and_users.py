# coding=utf-8

from sqlalchemy import Column, ForeignKey, Integer
from marshmallow import Schema, fields

from .entity import Base

class ArticlesAndUsers(Base):
    __tablename__ = 'articles_and_users'

    article_id = Column(Integer, ForeignKey("articles.id"), primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    def __init__(self, user_id, article_id):
        self.user_id = user_id
        self.article_id = article_id


class ArticlesAndUsersSchema(Schema):
    article_id = fields.Number()
    user_id = fields.Number()