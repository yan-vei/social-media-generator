from functools import partial
import re
import os


SENTENCES_PATTERN = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')


def load_stopwords(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')


def substitute_in_text(text):
    text = text.encode('ascii', errors='ignore').decode()
    text = re.sub(r"’", "'", text)
    text = re.sub(r"“", '"', text)
    text = text.lower()
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r"([A-Za-z]+)'s", r"\1 is", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"dont", " do not ", text)
    text = re.sub(r"didnt", " did not ", text)
    text = re.sub(r"wont", " will not ", text)
    text = re.sub(r"cant", " can not ", text)
    text = re.sub(r"shouldnt", " should not ", text)
    text = re.sub(r"thats", " that is ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'s", " is ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


def remove_stopwords(stopwords, tokens):
    result = []
    for token in tokens:
        if not token in stopwords:
            result.append(token)
    return result


def tokenize_into_sentences(text):
    return [sentence.strip() for sentence in re.split(SENTENCES_PATTERN, text) if sentence]


def preprocess_text(text):
    path = os.getcwd() + '\\data\\stopwords.txt'
    stop_words = load_stopwords(path)
    sentences = tokenize_into_sentences(text)
    sentences_processed = list(map(substitute_in_text, sentences))
    remove_stop = partial(remove_stopwords, stop_words)
    sentences_tokenized = [sentence for sentence in map(lambda x : remove_stop(x.split()), sentences_processed) if sentence]

    return sentences, sentences_tokenized


def preprocess_for_keywords(text):
    text = text.lower()
    text = re.sub("(\\d|\\W)+", " ", text)
    text = [text]

    return text