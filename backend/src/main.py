# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup

from backend.src.entities.text_entity import engine, Base
from services import articles_service, text_extracts_service, text_preprocessor
from getters import get_article_details, get_quotes, get_numbers, get_questions, get_first_sentence, get_key_sentences
from controllers import articles_controller, text_extracts_controller


app = Flask(__name__)
CORS(app)


@app.route('/articles')
def get_articles():
    articles = articles_controller.get_articles()

    return jsonify(articles)


@app.route('/articles', methods=['DELETE'])
def delete_article():
    id = request.args.get('id')
    articles_controller.delete_article_by_id(id)

    return(jsonify("Successfully deleted the article with the id " + id), 200)


@app.route('/articles', methods=['POST'])
def save_article():
    posted_article = articles_service.validate_schema(request)
    new_article = articles_controller.save_article(**posted_article)

    return jsonify(new_article), 201


@app.route('/text-extracts')
def get_text_extracts():
    text_extracts = text_extracts_controller.get_text_extracts()

    return jsonify(text_extracts), 200

@app.route('/text-extracts', methods=['POST'])
def save_text_extract():
    posted_text_extract = text_extracts_service.validate_schema(request)
    new_text_extract = text_extracts_controller.save_text_extract(**posted_text_extract)

    return jsonify(new_text_extract), 201


@app.route('/text-extracts', methods=['DELETE'])
def delete_text_extract():
    id = request.args.get('id')
    text_extracts_controller.delete_text_extract_by_id(id)

    return(jsonify("Successfully deleted the text extract with the id " + id), 200)


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
        data["numbers"] = get_numbers.get_numbers(data["sentences"])
        data["first_sentences"] = get_first_sentence.get_first_sentence(data["paragraphs"])

    #new_article = articles_controller.save_article(data["text"], data["url"], data["title"], added_by="yveitsman")

    return jsonify("OK"), 201


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug = True)