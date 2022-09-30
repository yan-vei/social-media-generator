# coding=utf-8

from sqlalchemy import Column, String, DateTime

from .entity import Entity, Base


class Article(Entity, Base):
    __tablename__ = 'articles'

    title = Column(String)
    text = Column(String)
    url = Column(String)
    header = Column(String)
    author = Column(String)
    published_on = Column(DateTime)

    def __init__(self, author, text, url,  added_by, published_on, title=None):
        Entity.__init__(self, added_by)
        self.text = text
        self.url = url
        self.author = author
        self.published_on = published_on
        self.title = title