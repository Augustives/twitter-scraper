import re
import nltk


def nltk_setup():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('tokenizers/corpus')
        nltk.data.find('tokenizers/stopwords')
    except LookupError:
        nltk.download('punkt')
        nltk.download('corpus')
        nltk.download('stopwords')


def remove_new_lines(text):
    return text.replace('\n', '')


def remove_urls(text):
    return re.sub(
        r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b',
        '',
        text
    )


def remove_stop_words(text):
    text = remove_urls(text)
    text = remove_new_lines(text)
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|^[https]')
    text_tokens = tokenizer.tokenize(text)

    tokens_without_sw = [
        word for word in text_tokens
        if word not in nltk.corpus.stopwords.words()
    ]

    return ' '.join(tokens_without_sw)
