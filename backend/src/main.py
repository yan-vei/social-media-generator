# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.article import Article, ArticleSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/articles')
def get_articles():
    # fetching from the database
    session = Session()
    article_objects = session.query(Article).all()

    # transforming into JSON-serializable objects
    schema = ArticleSchema(many=True)
    articles = schema.dump(article_objects)

    # serializing as JSON
    session.close()
    print(articles)
    return jsonify(articles)


@app.route('/articles', methods=['POST'])
def add_article():
    # mount exam object
    posted_article = ArticleSchema()\
        .load(request.get_json())
    print(posted_article)
    article = Article(**posted_article, added_by="yveitsman")

    # persist article
    session = Session()
    session.add(article)
    session.commit()

    # return created article
    new_article = ArticleSchema().dump(article)
    session.close()
    return jsonify(new_article), 201