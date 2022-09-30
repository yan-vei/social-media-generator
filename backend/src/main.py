# coding=utf-8
from datetime import datetime

from .entities.entity import Session, engine, Base
from .entities.article import Article

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
exams = session.query(Article).all()

#author, text, url,  added_by, published_on, header=None

if len(exams) == 0:
    # create and persist mock article
    python_article = Article("", "Thousands of young people have staged a coordinated “global climate strike” across Asia, Africa and Europe in a call for reparations for those worst affected by climate breakdown.", "https://www.theguardian.com/environment/2022/sep/23/thousands-call-for-climate-reparations-and-justice-in-global-protests", "yveitsman", datetime.now(), "Thousands call for ‘climate reparations and justice’ in global protests")
    session.add(python_article)
    session.commit()
    session.close()

# reload exams
articles = session.query(Article).all()

# show existing exams
print('### Articles:')
for article in articles:
    print(f'({article.id}) {article.title} - {article.text}')