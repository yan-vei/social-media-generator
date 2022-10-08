import numpy as np


def get_pagerank(matrix, eps=0.0001, d=0.85):
    n = len(matrix)
    probs = np.ones(n)/n
    for i in range(10):
        new_p = np.ones(n) * (1-d)/n + d*matrix.T.dot(probs)
        delta = abs(new_p-probs).sum()
        if delta <= eps:
            break
        probs = new_p
    return sorted(enumerate(new_p), key=lambda x: -x[1])


def get_cosine_similarity(tokens1, tokens2):
    vocab = set(tokens1 + tokens2)
    v1, v2 = [], []
    for word in vocab:
        v1.append(int(word in tokens1))
        v2.append(int(word in tokens2))
    return np.dot(v1, v2)/(np.linalg.norm(v1) * np.linalg.norm(v2))


def build_sim_matrix(sentences_tokenized, metrics):
    n = len(sentences_tokenized)
    matrix = np.ones((n, n))
    for i, sent1 in enumerate(sentences_tokenized):
        for j, sent2 in enumerate(sentences_tokenized):
            sim = metrics(sent1, sent2)
            matrix[i][j] = sim
            matrix[j][i] = sim
    return matrix


def get_textrank(sentences_tokenized):
    matrix = build_sim_matrix(sentences_tokenized, get_cosine_similarity)
    ranks = get_pagerank(matrix)
    return matrix, ranks


def get_key_sentences(sentences, sentences_tokenized, topn=3):
    matrix, ranks = get_textrank(sentences_tokenized)
    result = []
    for tuple in ranks[:topn]:
        index = tuple[0]
        result.append((sentences[index], tuple[1]))
    return result