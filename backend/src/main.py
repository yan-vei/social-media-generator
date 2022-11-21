# coding=utf-8

from flask import Flask, jsonify, request, make_response, session
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from bs4 import BeautifulSoup
from routes import articles_routes, text_extracts_routes, posts_routes, hashtags_routes
from backend.src.entities.entity import engine, Base
from services import text_preprocessor
from controllers import articles_extracts_users_controller, hashtags_controller, articles_controller, posts_controller, text_extracts_controller, users_controller
from getters import get_source, get_title, get_hashtags, get_article_details, get_url, get_quotes, get_numbers, get_questions, get_first_sentence, get_key_sentences, get_calls_to_action, get_page_details
import template_engine

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
bcrypt = Bcrypt(app)
CORS(app)

app.register_blueprint(articles_routes.articles)
app.register_blueprint(text_extracts_routes.text_extracts)
app.register_blueprint(posts_routes.posts)
app.register_blueprint(hashtags_routes.hashtags)

@app.route('/postsss', methods=['DELETE'])
def delete_posts():
    posts_controller.delete_posts_batch()
    return jsonify({'message': "OK"}), 200


@app.route('/hashtagsss', methods=['DELETE'])
def delete_hashtags():
    hashtags_controller.delete_hashtags_batch()
    return jsonify({'message': "OK"}), 200

@app.route('/posts', methods=['POST'])
def generate_post():
    data = request.get_json()
    new_article_id = None
    new_text_extract_id = None

    if "url" in data:
        articles = articles_controller.get_articles()
        for article in articles:
            if data["url"] == article["url"]:
                posts = posts_controller.get_posts_by_article_id(article['id'])
                posts.insert(0, template_engine.definition)
                hashtags = hashtags_controller.get_hashtags_by_article_id(article['id'])

                articles_extracts_users_controller.save_article_and_user(1, article['id'])

                result = {}
                result["tweets"] = posts
                result["hashtags"] = [get_hashtags.definition]
                for tag in hashtags:
                    result["hashtags"].append({tag['hashtag']: tag['score']})

                return make_response(jsonify(result), 200)

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

        new_article = articles_controller.save_article(data["text"], data["url"], data["Title"][1]["result"], added_by=1)
        articles_extracts_users_controller.save_article_and_user(1, new_article['id'])
        new_article_id = new_article['id']

    elif "text" in data and "title" in data and "source" in data:
        data["Title"] = get_title.get_excerpt_title(data["title"])

        text_extracts = text_extracts_controller.get_text_extracts()
        for text_extract in text_extracts:
            if text_extract['title'] == data["Title"][1]["result"]:
                posts = posts_controller.get_posts_by_text_extract_id(text_extract['id'])
                posts.insert(0, template_engine.definition)
                hashtags = hashtags_controller.get_hashtags_by_text_extract_id(text_extract['id'])

                articles_extracts_users_controller.save_text_extracts_and_user(1, text_extract['id'])

                result = {}
                result["tweets"] = posts
                result["hashtags"] = [get_hashtags.definition]
                for tag in hashtags:
                    result["hashtags"].append({tag['hashtag']: tag['score']})

                return jsonify(result), 200

        data["sentences"], data["sentences_tokenized"] = text_preprocessor.preprocess_text(data["text"])
        data["SOURCE"] = get_source.get_source(data["source"])

        new_text_extract = text_extracts_controller.save_text_extract(data["text"], data["Title"][1]["result"], added_by=1)
        articles_extracts_users_controller.save_text_extracts_and_user(1, new_text_extract['id'])
        new_text_extract_id = new_text_extract['id']

    else:
        return make_response(jsonify({'message': 'Invalid format'}), 400)


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
        data["Hashtags"].pop(0)
        for tweet in data["Tweets"]:
            posts_controller.save_post(tweet['post'], tweet['score'], tweet['length'], tweet['notes'], tweet['template'], article_id=new_article_id, text_extract_id=new_text_extract_id)
        for hashtag in data["Hashtags"]:
            for h, score in hashtag.items():
                hashtags_controller.save_hashtag(new_article_id, new_text_extract_id, h, score)

    return make_response(jsonify(result), 201)

@app.route('/users/register', methods=['POST'])
def register():
    data = request.get_json()
    if "username" in data and "email" in data and "password" in data:
        new_user = users_controller.save_user(data["email"], data["password"], data["username"])
        if new_user != "Already exists":
            return make_response(jsonify({'message': 'Created new user with username ' + new_user['username'],
                                          'token': new_user["token"]}), 201)
    else:
        return make_response(jsonify({'error': 'Invalid user data'}), 400)

    return make_response(jsonify({'message': 'User already exists'}), 200)


@app.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    status = False
    if "username" in data and "password" in data:
        user = users_controller.login_user(data["username"], data["password"])
        if user:
            session['logged_in'] = True
            session['token'] = user['token']
            status = True
    else:
        return make_response(jsonify({'error': 'Invalid parameters passed'}), 400)

    return jsonify({'result': status, 'token': session['token']})


@app.route('/users/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('token', None)
    return make_response(jsonify({'message': 'success'}), 200)


@app.route('/users/status')
def status():
    if session.get('logged_in'):
        if session['logged_in']:
            return make_response(jsonify({'message': 'success'}), 200)
    else:
        return make_response(jsonify({'message': 'failed'}), 500)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug = True)