from backend.src.entities.post import Post, PostSchema
from backend.src.entities.text_entity import Session


def save_post(text, article_id, text_extract_id, added_by):
    post = Post(text, article_id, text_extract_id, added_by)

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


def delete_post_by_id(id):
    session = Session()
    session.query(Post).filter_by(id=id).delete()

    session.commit()
    session.close()

    return id