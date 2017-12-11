from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

import auth_twitter as at


class listener(StreamListener):
    # def on_data(self, data):
    #     print(data)
    #     return(True)

    def on_error(self, status):
        print(status)

    def on_data(self, data):

        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]

        # c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
        #     (time.time(), username, tweet))
        #
        # conn.commit()

        print((username, tweet, time))

        return True

twitterStream = Stream(at.auth, listener())
twitterStream.filter(track=["johnny"])
