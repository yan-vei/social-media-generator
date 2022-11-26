from entities.post import Post, PostSchema
from entities.entity import Session


def save_post(post, score, length, notes, template, article_id, text_extract_id,):
    post = Post(post, score, length, notes, template, article_id, text_extract_id)

    session = Session()
    session.add(post)
    session.commit()

    new_post = PostSchema().dump(post)
    session.close()

    return new_post


def get_posts():
    session = Session()
    posts_objects = session.query(Post).all()

    schema = PostSchema(many=True)
    posts = schema.dump(posts_objects)

    session.close()

    return posts


def delete_posts_by_article_id(id):
    session = Session()
    session.query(Post).filter_by(article_id=id).delete()

    session.commit()
    session.close()

    return id


def delete_posts_by_text_extract_id(id):
    session = Session()
    session.query(Post).filter_by(text_extract_id=id).delete()

    session.commit()
    session.close()

    return id

def get_posts_by_article_id(id):
    session = Session()
    posts_objects = session.query(Post).with_entities(Post.post, Post.template, Post.length, Post.notes, Post.score).filter_by(article_id=id)

    schema = PostSchema(many=True)
    posts = schema.dump(posts_objects)

    session.commit()
    session.close()

    return posts

def get_posts_by_text_extract_id(id):
    session = Session()
    posts_objects = session.query(Post).with_entities(Post.post, Post.template, Post.length, Post.notes, Post.score).filter_by(text_extract_id=id)

    schema = PostSchema(many=True)
    posts = schema.dump(posts_objects)

    session.commit()
    session.close()

    return posts

def delete_post_by_id(id):
    session = Session()
    session.query(Post).filter_by(id=id).delete()

    session.commit()
    session.close()

    return id

def delete_posts_batch():
    session = Session()
    session.query(Post).delete()

    session.commit()
    session.close()