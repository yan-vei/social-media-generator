# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup

from backend.src.entities.entity import engine, Base
from routes import articles_routes, text_extracts_routes, posts_routes
from services import text_preprocessor
from getters import get_article_details, get_quotes, get_numbers, get_questions, get_first_sentence, get_key_sentences


app = Flask(__name__)

app.register_blueprint(articles_routes.articles)
app.register_blueprint(text_extracts_routes.text_extracts)
app.register_blueprint(posts_routes.posts)
CORS(app)


@app.route('/post', methods=['POST'])
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
        data["numbers"] = get_numbers.get_numbers(data["sentences"])
        data["first_sentences"] = get_first_sentence.get_first_sentence(data["paragraphs"])

    #new_article = articles_controller.save_article(data["text"], data["url"], data["title"], added_by="yveitsman")

    return jsonify("OK"), 201


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug = True)