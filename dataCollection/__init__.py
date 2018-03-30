import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from nltk import word_tokenize
import pickle

open_pickle = open("word_features11k.pickle", "rb")
word_features = pickle.load(open_pickle)
open_pickle.close()

def CollectionData(consumer_key,consumer_secret,access_token,access_secret,list):
    # consumer_key = "WA0tLIpdYD1Mqct8h6B3VNHTi"
    # consumer_secret = "mRXOdvqM1kmrBrIWoJhWlXAVFXjSuQLhuzy8KLAHGeGcyK1UPc"
    # access_token = "794403529947430912-UaR2KheAZ8OLkSfE4ZNUTp4MkRtUuQ5"
    # access_secret = "gEZIDYfKR9vXhvDUGvi4TjKbQcgqjZjUINFnW5vpx4Plm"
    
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)

    api = tweepy.API(auth)
    class MyListener(StreamListener):
        def on_data(self,data):
            try:
                with open('InputFile/input.json','a') as f:
                    f.write(data)
                    return True
            except BaseException as e:
                print("Error on_data: %s" %str(e))
            return True
        def on_error(self,status):
            print(status)
            return  True

    twitter_stream = Stream(auth,MyListener())
    twitter_stream.filter(track=[list],async=True)


def find_features(document):
    # words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in document)
    print(features)
    return features