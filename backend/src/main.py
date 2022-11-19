# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup

from backend.src.entities.entity import engine, Base
from routes import articles_routes, text_extracts_routes, posts_routes
from services import text_preprocessor
from controllers import articles_controller, posts_controller, text_extracts_controller
from getters import get_source, get_title, get_hashtags, get_article_details, get_url, get_quotes, get_numbers, get_questions, get_first_sentence, get_key_sentences, get_calls_to_action, get_page_details
import template_engine

app = Flask(__name__)

app.register_blueprint(articles_routes.articles)
app.register_blueprint(text_extracts_routes.text_extracts)
app.register_blueprint(posts_routes.posts)
CORS(app)


@app.route('/posts', methods=['POST'])
def generate_post():
    data = request.get_json()
    new_article_id = None
    new_text_extract_id = None

    if "url" in data:
        data["markup"] = get_article_details.download_url(data["url"])
        data["soup"] = BeautifulSoup(data["markup"], 'html5lib')
        data["paragraphs"] = get_article_details.get_article_paragraphs(data["soup"])
        data["text"] = get_article_details.extract_text(data["paragraphs"])
        data["sentences"], data["sentences_tokenized"] = text_preprocessor.preprocess_text(data["text"])

        data["URL"] = get_url.get_url(data["url"])
        data["FirstSentence"] = get_first_sentence.get_first_sentence(data["paragraphs"])
        data["Quotes"] = get_quotes.get_quotes(data["paragraphs"])
        data["Page"] = get_page_details.get_page_details(data["soup"])
        data["Title"] = get_title.get_title(data["soup"], data["FirstSentence"])

        articles = articles_controller.get_articles()
        saved = False
        for article in articles:
            if data["url"] == article["url"]:
                saved = True
                break
        if not saved:
            new_article = articles_controller.save_article(data["text"], data["url"], data["Title"][1]["result"], added_by="yveitsman")
            new_article_id = new_article['id']

    elif "text" in data and "title" in data and "source" in data:
        data["sentences"], data["sentences_tokenized"] = text_preprocessor.preprocess_text(data["text"])
        data["Title"] = get_title.get_excerpt_title(data["title"])
        data["SOURCE"] = get_source.get_source(data["source"])

        text_extracts = text_extracts_controller.get_text_extracts()
        saved = False
        for text_extract in text_extracts:
            if text_extract['title'] == data["Title"][1]["result"]:
                saved = True
                break
        if not saved:
            new_text_extract = text_extracts_controller.save_text_extract(data["text"], data["Title"][1]["result"], added_by="yveitsman")
            new_text_extract_id = new_text_extract['id']

    else:
        return jsonify({'message': 'Invalid format'}), 400


    data["KeySentence"] = get_key_sentences.get_key_sentences(data["sentences"], data["sentences_tokenized"])
    data["Question"] = get_questions.get_questions(data["text"])
    data["Number"] = get_numbers.get_numbers(data["sentences"])
    data["AlwaysValidCTAs"] = get_calls_to_action.get_calls_to_action()

    data["Tweets"] = template_engine.get_tweets(data)
    data["Hashtags"] = get_hashtags.get_hashtags(data['text'])

    result = {}
    result["tweets"] = data["Tweets"]
    result["hashtags"] = data["Hashtags"]

    if new_article_id != None or new_text_extract_id != None:
        data["Tweets"].pop(0)
        for tweet in data["Tweets"]:
            new_post = posts_controller.save_post(tweet['result'], text_extract_id=new_text_extract_id, article_id=new_article_id)

    return jsonify(result), 201


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug = True)