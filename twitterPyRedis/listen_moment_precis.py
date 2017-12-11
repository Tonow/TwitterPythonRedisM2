import tweepy
import auth_twitter as at
import connection_to_redis as redis

query = 'python'
max_tweets = 20

public_tweets = [status for status in tweepy.Cursor(at.api.search, q=query).items(max_tweets)]

# Results
numero = 1
for tweet in public_tweets:
    print (f"message n: {numero}")
    print(f"id: {tweet.id}  texte: {tweet.text}")
    idtweetredis = "tweetid" + str(tweet.id)
    redis.r.set(idtweetredis, tweet.text)
    idredis = redis.r.get(idtweetredis)
    print(f"id redis = {idredis}")
    numero = numero + 1
