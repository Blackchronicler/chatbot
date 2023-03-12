import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

# Stemming the words and removing duplicate elements
#words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
#words = sorted(list(set(words)))
#labels = sorted(labels)

def theStemmer (words:list):
    new_words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    new_words = sorted(list(set(new_words)))
    return new_words

def labelSorter (labels:list):
    sorted_labels = sorted(labels)
    return sorted_labels

if __name__ == "__main__":
    theStemmer()
    labelSorter()