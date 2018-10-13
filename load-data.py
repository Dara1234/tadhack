from __future__ import unicode_literals

import spacy
spacy.load('en')
from spacy.lang.en import English
parser = English()
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import random
import os
import codecs
from gensim import corpora
import pickle
import gensim
import csv


def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


# for w in ['dogs', 'ran', 'discouraged']:
#     print(w, get_lemma(w), get_lemma2(w))

nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))


def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens


text_data = []
writer = csv.writer(
    open("/Users/dara/Desktop/Projects/python-extractor/new-dataset.csv", 'w'))
with codecs.open(os.path.abspath("/Users/dara/Desktop/Projects/python-extractor/celcomthree.csv")) as f:
    for line in f:
        u = unicode(line, "utf-8")
        tokens = prepare_text_for_lda(u)
        # if random.random() > .99:
        print(tokens)
        writer.writerow(tokens)
        text_data.append(tokens)


# To hold the counts of each word


dictionary = corpora.Dictionary(text_data)

corpus = [dictionary.doc2bow(text) for text in text_data]

pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')

NUM_TOPICS = 50
ldamodel = gensim.models.ldamodel.LdaModel(
    corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=50)
ldamodel.save('model5.gensim')

topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)


# new_doc = 'Practical Bayesian Optimization of Machine Learning Algorithms'
# new_doc = prepare_text_for_lda(new_doc)
# new_doc_bow = dictionary.doc2bow(new_doc)
# print(new_doc_bow)
# print(ldamodel.get_document_topics(new_doc_bow))

# ldamodel = gensim.models.ldamodel.LdaModel(
#     corpus, num_topics=3, id2word=dictionary, passes=15)
# ldamodel.save('model3.gensim')
# topics = ldamodel.print_topics(num_words=4)
# for topic in topics:
#     print(topic)


# dictionary = gensim.corpora.Dictionary.load('dictionary.gensim')
# corpus = pickle.load(open('corpus.pkl', 'rb'))
# lda = gensim.models.ldamodel.LdaModel.load('model5.gensim')
