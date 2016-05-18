import nltk
import random
from nltk.corpus import movie_reviews
#movie_reviews contains 1000 positive, 1000 negative reviews
#features - presence or absence of words; category is the tag (positive/negative)
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

#print(documents[1])

#we wnt to create a list of typical/common or most popular words for positive and negative texts, and then
#simply check for each test data, if it contains more of those positive words, or the typical negative indicating words more
#this is naive bayes classficiation

#firstly, we compile a massive list of wall words
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

#From here, we can perform a frequency distribution, to then find out the most common words.

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
#how many occurences a word has?
print(all_words["stupid"])

#till now, we have not done the common words according to positive/negative...