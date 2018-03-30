from statistics import mode
import algorithm
from new import *
import dataCollection as DC
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

voted_classifier = VoteClassifier(algorithm.NaiveBayes,
                                  algorithm.Bnaivebayes,
                                  algorithm.Linear_SVC,
                                  algorithm.LogisticR_classifier,
                                  algorithm.MNB_classifier
                                  )


def voted_classifier_text(text):
    featureset = DC.find_features(text)
    return voted_classifier.classify(featureset)
