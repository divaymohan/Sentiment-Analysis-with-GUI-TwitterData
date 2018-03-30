from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time

analyzer = SentimentIntensityAnalyzer()

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()

#consumer key, consumer secret, access token, access secret.
ckey="WA0tLIpdYD1Mqct8h6B3VNHTi"
csecret="mRXOdvqM1kmrBrIWoJhWlXAVFXjSuQLhuzy8KLAHGeGcyK1UPc"
atoken="794403529947430912-UaR2KheAZ8OLkSfE4ZNUTp4MkRtUuQ5"
asecret="gEZIDYfKR9vXhvDUGvi4TjKbQcgqjZjUINFnW5vpx4Plm"


# consumer_key = "WA0tLIpdYD1Mqct8h6B3VNHTi"
# consumer_secret = "mRXOdvqM1kmrBrIWoJhWlXAVFXjSuQLhuzy8KLAHGeGcyK1UPc"
# access_token = "794403529947430912-UaR2KheAZ8OLkSfE4ZNUTp4MkRtUuQ5"
# access_secret = "gEZIDYfKR9vXhvDUGvi4TjKbQcgqjZjUINFnW5vpx4Plm"

class listener(StreamListener):

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms, tweet, sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                  (time_ms, tweet, sentiment))
            conn.commit()

        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)


while True:

    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=['black'])
    except Exception as e:
        print(str(e))
        time.sleep(5)