import numpy as np
from backend.src.services import emoji_counter

definition = {
    'type': 'KeySentence',
    'description': 'Get key sentences from the data.',
    'score': 4,
    'score description': 'Block scores according to how pagerank algorithm ranks it.',
    'notes': 'Description of how the getter was scored',
    'generatedLength': 0
}

def evaluate(matrix, eps=0.0001, d=0.85):
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
    ranks = evaluate(matrix)
    return matrix, ranks


def get_key_sentences(sentences, sentences_tokenized):
    result = [definition]

    matrix, ranks = get_textrank(sentences_tokenized)
    topn = 3 if int(len(sentences) * 0.1) < 3 else int(len(sentences) * 0.1)

    for pair in ranks[:topn]:
        index = pair[0]
        emoji_count = emoji_counter.count_emoji(sentences[index])
        result.append({
            "result": sentences[index],
            "score": int(pair[1]),
            "notes": "Score assigned by pagerank. ",
            "emoji_count": emoji_count
        })

    result[0]["generatedLength"] = len(result) - 1

    return result