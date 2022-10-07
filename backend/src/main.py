# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.article import Article, ArticleSchema
from .getters import getArticleDetails


# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/articles')
def get_articles():
    session = Session()
    article_objects = session.query(Article).all()

    schema = ArticleSchema(many=True)
    articles = schema.dump(article_objects)

    session.close()
    print(articles)
    return jsonify(articles)


@app.route('/posts', methods=['POST'])
def generate_post():
    data = request.get_json()
    if "url" in data:
        data["markup"] = getArticleDetails.download_url(data["url"])
        data["paragraphs"] = getArticleDetails.get_article_text(data["markup"])
        data["text"] = getArticleDetails.get_article_text(data["paragraphs"])
    print(data["text"])


    #posted_article = ArticleSchema()\
     #   .load(request.get_json())
    #print(posted_article)
    #article = Article(**posted_article, added_by="yveitsman")

    #session = Session()
    #session.add(article)
   # session.commit()

    #new_article = ArticleSchema().dump(article)
   # session.close()
    return jsonify("Good"), 201