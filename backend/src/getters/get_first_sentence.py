import re

SENTENCE_PATTERN = re.compile(r"[A-Z][^\.!?]*[\.!?]")
QUOTATION_MARKS = """"'“”"""


def get_first_sentence(paragraphs):
    first_sentences = []
    for paragraph in paragraphs:
        text = paragraph.get_text(' ')
        if text[0] not in QUOTATION_MARKS:
            first_sentence = re.search(SENTENCE_PATTERN, text)
            if first_sentence:
                first_sentences.append(first_sentence.group())

    return first_sentences

