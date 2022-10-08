# coding=utf-8

import requests
import re


NEGATIVE = re.compile(".*comment.*|.*footer.*|.*foot.*|.*cloud.*|.*head.*|.*side.*|.*menu.*")
POSITIVE = re.compile(".*post.*|.*hentry.*|.*entry.*|.*content.*|.*text.*|.*body.*|.*article.*|.*summary.*")
IRRELEVANT = ['script', 'label', 'button', 'time', 'input', 'footer', 'icon', 'form']
TEXT_TAGS = ['p', 'h2', 'h3']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
}

def download_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 406 or r.status_code == 403:
            r = requests.get(url, headers=HEADERS)
        elif 'Connection' in r.headers.keys():
            if r.headers['Connection'] == 'close':
                r = requests.get(url, headers=HEADERS)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    data = r.text
    return data

def get_article_title(soup):
    soup_title = soup.find('h1')
    return soup_title.get_text(' ')

def get_article_paragraphs(soup):
    resulting_pars = []
    paragraphs = []

    soup_tags = soup.find_all()
    for tag in soup_tags:
        if tag.name in TEXT_TAGS:
            paragraphs.append(tag)

    for paragraph in paragraphs:
        children = paragraph.children

        for child in children:
            if child.name in IRRELEVANT:
                child.extract()

        parent = paragraph.parent

        if parent.name == 'blockquote':
            quote = parent.get_text()
            resulting_pars.append('<p>"' + quote + '"</p>')
            continue

        parent.score = 0

        if parent.has_attr("class"):
            if NEGATIVE.match(str(parent["class"])):
                parent.score -= 50
            elif POSITIVE.match(str(parent["class"])):
                parent.score += 25

        if parent.has_attr("id"):
            if NEGATIVE.match(str(parent["id"])):
                parent.score -= 50
            elif POSITIVE.match(str(parent["id"])):
                parent.score += 25

        if parent.name in IRRELEVANT and parent.score > 0:
            parent.score -= 50

        if parent.score >= 0:
            if len(paragraph.get_text(' ').split()) > 10:
                resulting_pars.append(paragraph)

    return resulting_pars


def extract_text(pars):
    text = ""

    for par in pars:
        if type(par) != str:
            text += ' ' + par.get_text(' ').strip()
        else:
            text += ' ' + par.strip()

    return text