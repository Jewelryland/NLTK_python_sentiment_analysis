import nltk
import random
from nltk.corpus import movie_reviews
import pickle

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]
#classifier = nltk.NaiveBayesClassifier.train(training_set)
#X:
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()


print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)

#Training classifiers and machine learning algorithms can take a very long time, especially if you're training against a larger data set.
# use the Pickle module to go ahead and serialize our classifier object, so that all we need to do is load that file in real quick.

#So, how do we do this? The first step is to save the object. To do this, first you need to import pickle at the top of your script, then,
#after you have trained with .train() the classifier, you can then call the following lines:


#save_classifier = open("naivebayes.pickle","wb")               #This opens up a pickle file, preparing to write in bytes some data. Then, we use pickle.dump() to dump the data.
#pickle.dump(classifier, save_classifier)                       #The first parameter to pickle.dump() is what are you dumping, the second parameter is where are you dumping it.
#save_classifier.close()                                        #we close the file as we're supposed to, and that is that, we now have a pickled, or serialized, object saved in our script's directory!



#run the above, then we have the saved object in pickle file, now we can comment it out and use this saved classifier as done above at X.