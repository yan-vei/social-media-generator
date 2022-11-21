from backend.src.entities.articles_and_users import ArticlesAndUsersSchema, ArticlesAndUsers
from backend.src.entities.text_extracts_and_users import  TextExtractsAndUsersSchema, TextExtractsAndUsers
from backend.src.entities.entity import Session


def save_article_and_user(user_id, article_id):
    try:
        articleAndUser = ArticlesAndUsers(user_id, article_id)

        session = Session()
        session.add(articleAndUser)
        session.commit()

        new_article = ArticlesAndUsersSchema().dump(articleAndUser)
        session.close()

        return new_article
    except:
        session = Session()
        article = session.query(ArticlesAndUsers).filter_by(article_id=article_id)
        session.close()

        return article


def get_articles_and_users():
    session = Session()
    article_objects = session.query(ArticlesAndUsers).all()

    schema = ArticlesAndUsersSchema(many=True)
    articles = schema.dump(article_objects)

    session.close()

    return articles


def get_articles_by_user_id(user_id):
    session = Session()
    article_objects = session.query(ArticlesAndUsers).filter_by(user_id=user_id)

    schema = ArticlesAndUsersSchema(many=True)
    articles = schema.dump(article_objects)

    session.close()

    return articles

def save_text_extracts_and_user(user_id, text_extract_id):
    try:
        textExtractAndUser = TextExtractsAndUsers(user_id, text_extract_id)

        session = Session()
        session.add(textExtractAndUser)
        session.commit()

        new_text_extract = TextExtractsAndUsersSchema().dump(textExtractAndUser)
        session.close()

        return new_text_extract
    except:
        session = Session()
        text_extract = session.query(TextExtractsAndUsers).filter_by(text_extract_id=text_extract_id)
        session.close()

        return text_extract

def get_text_extracts_and_users():
    session = Session()
    text_extracts_objects = session.query(TextExtractsAndUsers).all()

    schema = TextExtractsAndUsersSchema(many=True)
    articles = schema.dump(text_extracts_objects)

    session.close()

    return articles


def get_text_extracts_by_user_id(user_id):
    session = Session()
    text_extracts_objects = session.query(TextExtractsAndUsers).filter_by(user_id=user_id)

    schema = TextExtractsAndUsersSchema(many=True)
    text_extracts = schema.dump(text_extracts_objects)

    session.close()

    return text_extracts



