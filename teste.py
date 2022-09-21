import pandas as pd
import tweepy as tw
import config_t

client = tw.Client(bearer_token=config_t.ACADEMIC_BEARER_TOKEN)

query ='bolsonaro place_country:BR'

tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions = ['author_id'])

users = {u['id']: u for u in tweets.includes['users']}

for tweet in tweets.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print (tweet.id)
        print (user.username)
