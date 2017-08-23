import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), cat) 
            for cat in movie_reviews.categories()
            for fileid in movie_reviews.fileids(cat)]

print(documents[0])