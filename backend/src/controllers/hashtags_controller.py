from backend.src.entities.hashtag import Hashtag, HashtagSchema
from backend.src.entities.entity import Session


def save_hashtag(article_id, text_extract_id, hashtag, score):
    hashtag = Hashtag( article_id, text_extract_id, hashtag, score)

    session = Session()
    session.add(hashtag)
    session.commit()

    new_hashtag = HashtagSchema().dump(hashtag)
    session.close()

    return new_hashtag


def get_hashtags():
    session = Session()
    hashtags_objects = session.query(Hashtag).all()

    schema = HashtagSchema(many=True)
    hashtags = schema.dump(hashtags_objects)

    session.close()

    return hashtags


def get_hashtags_by_article_id(id):
    session = Session()
    posts_objects = session.query(Hashtag).with_entities(Hashtag.hashtag, Hashtag.score).filter_by(article_id=id)

    schema = HashtagSchema(many=True)
    hashtags = schema.dump(posts_objects)

    session.commit()
    session.close()

    return hashtags


def get_hashtags_by_text_extract_id(id):
    session = Session()
    posts_objects = session.query(Hashtag).with_entities(Hashtag.hashtag, Hashtag.score).filter_by(text_extract_id=id)

    schema = HashtagSchema(many=True)
    hashtags = schema.dump(posts_objects)

    session.commit()
    session.close()

    return hashtags


def delete_hashtag_by_id(id):
    session = Session()
    session.query(Hashtag).filter_by(id=id).delete()

    session.commit()
    session.close()

    return id


def delete_hashtags_batch():
    session = Session()
    session.query(Hashtag).delete()

    session.commit()
    session.close()


def delete_hashtags_by_text_extract_id(id):
    session = Session()
    session.query(Hashtag).filter_by(text_extract_id=id).delete()

    session.commit()
    session.close()

    return id


def delete_hashtags_by_article_id(id):
    session = Session()
    session.query(Hashtag).filter_by(article_id=id).delete()

    session.commit()
    session.close()

    return id