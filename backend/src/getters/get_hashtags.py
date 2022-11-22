from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import os
from backend.src.services.text_preprocessor import load_stopwords

definition = {
    'type': 'Hashtags',
    'description': 'Get hashtags from the text.',
    'score description': 'Hashtags are score automatically by TF-IDF',
    'notes': 'Description of how the getter was scored',
    'generatedLength': 0
}


def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_topn_from_vector(feature_names, sorted_items, topn):
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    results = []
    for idx in range(len(feature_vals)):
        results.append({feature_vals[idx]:score_vals[idx]})

    return results


def get_hashtags(text):
    path = os.getcwd() + '\\data\\stopwords.txt'
    stop_words = load_stopwords(path)

    cv = CountVectorizer(stop_words=stop_words)
    word_count_vector = cv.fit_transform([text])
    tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
    tfidf_transformer.fit(word_count_vector)

    feature_names = cv.get_feature_names_out()

    tf_idf_vector = tfidf_transformer.transform(cv.transform([text]))

    sorted_items = sort_coo(tf_idf_vector.tocoo())

    result = extract_topn_from_vector(feature_names, sorted_items, 10)

    result.insert(0, definition)

    result[0]["generatedLength"] = len(result) -1

    return result