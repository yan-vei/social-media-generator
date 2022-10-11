# coding=utf-8

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime

class TextEntity():
    id = Column(Integer, primary_key=True)
    added_at = Column(DateTime)

    def __init__(self):
        self.added_at = datetime.now()