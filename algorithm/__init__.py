import pickle
import nltk
from statistics import mode

from new import *
import dataCollection as DC

classifier_f = open("pickle/naivebayes.pickle", "rb")
NaiveBayes = pickle.load(classifier_f)
classifier_f.close()

classifier1 = open("pickle/BNB_classifier.pickle","rb")
Bnaivebayes = pickle.load(classifier1)
classifier1.close()

classifier1 = open("pickle/LinearSVC_classifier.pickle","rb")
Linear_SVC = pickle.load(classifier1)
classifier1.close()

classifier1 = open("pickle/LogisticRegression_classifier.pickle","rb")
LogisticR_classifier = pickle.load(classifier1)
classifier1.close()

classifier1 = open("pickle/MNB_classifier.pickle","rb")
MNB_classifier = pickle.load(classifier1)
classifier1.close()

classifier1 = open("pickle/testing.pickle","rb")
testing = pickle.load(classifier1)
classifier1.close()

def Accuracy(classifier):
    accuracy = (nltk.classify.accuracy(classifier, testing)) * 100
    print(type(accuracy))
    return accuracy

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

voted_classifier = VoteClassifier(NaiveBayes,
                                  Bnaivebayes,
                                  Linear_SVC,
                                  LogisticR_classifier,
                                  MNB_classifier
                                  )


def voted_classifier_text(text):
    featureset = DC.find_features(text)
    return voted_classifier.classify(featureset)



