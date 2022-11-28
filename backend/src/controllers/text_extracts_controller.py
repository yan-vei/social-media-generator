from entities.text_extract import TextExtract, TextExtractSchema
from entities.entity import Session


def save_text_extract(text, title, source, added_by):
    text_extract = TextExtract(text, title, source, added_by)

    session = Session()
    session.add(text_extract)
    session.commit()

    new_text_extract = TextExtractSchema().dump(text_extract)
    session.close()

    return new_text_extract


def get_text_extracts():
    session = Session()
    text_extracts_objects = session.query(TextExtract).all()

    schema = TextExtractSchema(many=True)
    text_extracts = schema.dump(text_extracts_objects)

    session.close()
    return text_extracts


def get_text_extracts_by_ids(ids):
    session = Session()
    schema = TextExtractSchema(many=True)

    text_extracts_by_user = session.query(TextExtract).filter(TextExtract.id.in_(ids))

    text_extracts_objects = schema.dump(text_extracts_by_user)

    session.close()

    return text_extracts_objects


def delete_text_extract_by_id(id):
    session = Session()
    session.query(TextExtract).filter_by(id=id).delete()

    session.commit()
    session.close()

    return id