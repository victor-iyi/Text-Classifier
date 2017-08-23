import nltk
from nltk.corpus import movie_reviews
import random

documents = [(list(movie_reviews.words(fileid)), cat)
              for cat in movie_reviews.categories()
              for fileid in movie_reviews.fileids(cat)]

all_words = [w for w in movie_reviews.words()]
all_words = nltk.FreqDist(all_words)
