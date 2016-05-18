from nltk.corpus import wordnet
syns = wordnet.synsets("program")
#print(syns)

#synset
print(syns[0].name())

# just the word
print(syns[0].lemmas()[0].name())

# definition
print(syns[0].definition())

#example
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#Next, we can also easily use WordNet to compare the similarity of two words and their tenses, by incorporating the Wu and Palmer method for semantic related-ness.

#Let's compare the noun of "ship" and "boat:"

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))