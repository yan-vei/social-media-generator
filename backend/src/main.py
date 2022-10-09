# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup

from .entities.entity import engine, Base
from .getters import get_article_details
from .getters import get_key_sentences
from .getters import get_questions
from .getters import get_quotes
from .controllers import articles_controller
from .helpers import text_preprocessor


# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/articles')
def get_articles():
    articles = articles_controller.get_articles()

    return jsonify(articles)


@app.route('/articles', methods=['DELETE'])
def delete_article():
    id = request.args.get('id')
    articles_controller.delete_article_by_id(id)

    return(jsonify("Successfully deleted the article with the id " + id), 200)


@app.route('/posts', methods=['POST'])
def generate_post():
    data = request.get_json()
    if "url" in data:
        data["markup"] = get_article_details.download_url(data["url"])
        data["soup"] = BeautifulSoup(data["markup"], 'html5lib')
        data["paragraphs"] = get_article_details.get_article_paragraphs(data["soup"])
        data["text"] = get_article_details.extract_text(data["paragraphs"])
        data["title"] = get_article_details.get_article_title(data["soup"])
        data["sentences"], data["sentences_tokenized"] = text_preprocessor.preprocess_text(data["text"])

        data["key_sentences"] = get_key_sentences.get_key_sentences(data["sentences"], data["sentences_tokenized"])
        data["questions"] = get_questions.get_questions(data["text"])
        data["quotes"] = get_quotes.get_quotes(data["sentences"])



    #new_article = articles_controller.save_article(data["text"], data["url"], data["title"], added_by="yveitsman")

    return jsonify("OK"), 201