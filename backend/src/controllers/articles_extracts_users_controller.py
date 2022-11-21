from backend.src.entities.articles_and_users import ArticlesAndUsersSchema, ArticlesAndUsers
from backend.src.entities.text_extracts_and_users import  TextExtractsAndUsersSchema, TextExtractsAndUsers
from backend.src.entities.entity import Session


def save_article_and_user(user_id, article_id):
    articleAndUser = ArticlesAndUsers(user_id, article_id)

    session = Session()
    session.add(articleAndUser)
    session.commit()

    new_article = ArticlesAndUsersSchema().dump(articleAndUser)
    session.close()

    return new_article


def get_articles_and_users():
    session = Session()
    article_objects = session.query(ArticlesAndUsers).all()

    schema = ArticlesAndUsersSchema(many=True)
    articles = schema.dump(article_objects)

    session.close()

    return articles


def save_text_extracts_and_user(user_id, text_extract_id):
    textExtractAndUser = TextExtractsAndUsers(user_id, text_extract_id)

    session = Session()
    session.add(textExtractAndUser)
    session.commit()

    new_article = TextExtractsAndUsersSchema().dump(textExtractAndUser)
    session.close()

    return new_article


def get_text_extracts_and_users():
    session = Session()
    text_extracts_objects = session.query(TextExtractsAndUsers).all()

    schema = TextExtractsAndUsersSchema(many=True)
    articles = schema.dump(text_extracts_objects)

    session.close()

    return articles

