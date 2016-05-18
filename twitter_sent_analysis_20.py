from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="Rc3kyaAZwn8PCqFCMbfX4nmwc"
csecret="bzRKpe0fEPjV91bdOYnqSbE40TjKprSYJRQof1lTKOR9NNMoEN"
atoken="733019438363070465-x95WQZtJl1l5Et01Wb1aVtENdCvGAen"
asecret="q3S1FKwYB7QeclmB3yvx9mqdBiF4xQWk1DuWqrYffC35x"



class listener(StreamListener):

    def on_data(self, data):
        try:

            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out2.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True




    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])