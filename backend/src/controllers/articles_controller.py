from ..entities.article import Article, ArticleSchema
from ..entities.entity import Session

def save_article(text, url, title, added_by):
    article = Article(text, url, title, added_by)

    session = Session()
    session.add(article)
    session.commit()

    new_article = ArticleSchema().dump(article)
    session.close()

    return new_article


def get_articles():
    session = Session()
    article_objects = session.query(Article).all()

    schema = ArticleSchema(many=True)
    articles = schema.dump(article_objects)

    session.close()

    return articles


def delete_article_by_id(id):
    session = Session()
    session.query(Article).filter_by(id=id).delete()

    session.commit()
    session.close()

    return id