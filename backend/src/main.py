# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup

from backend.src.entities.entity import engine, Base
from routes import articles_routes, text_extracts_routes, posts_routes
from services import text_preprocessor
from getters import get_hashtags, get_article_details, get_url, get_quotes, get_numbers, get_questions, get_first_sentence, get_key_sentences, get_calls_to_action, get_page_details
import template_engine

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

    data["URL"] = get_url.get_url(data["url"])
    data["KeySentence"] = get_key_sentences.get_key_sentences(data["sentences"], data["sentences_tokenized"])
    data["Question"] = get_questions.get_questions(data["text"])
    data["Number"] = get_numbers.get_numbers(data["sentences"])
    data["FirstSentence"] = get_first_sentence.get_first_sentence(data["paragraphs"])
    data["AlwaysValidCTAs"] = get_calls_to_action.get_calls_to_action()
    data["Quotes"] = get_quotes.get_quotes(data["paragraphs"])
    data["Page"] = get_page_details.get_page_details(data["soup"])

    data["Tweets"] = template_engine.get_tweets(data)
    data["Hashtags"] = get_hashtags.get_hashtags(data['text'])
    print(data["Hashtags"])

    #new_article = articles_controller.save_article(data["text"], data["url"], data["title"], added_by="yveitsman")

    return jsonify("OK"), 201


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug = True)