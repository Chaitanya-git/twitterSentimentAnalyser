from textblob import TextBlob
import tweepy, csv

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

general_polarity = 0.0
general_subjectivity = 0.0

with open( 'tweets.csv', 'w', newline='' ) as csvfile:
    for tweet in public_tweets:
        writer = csv.writer( csvfile, delimiter=',' )
        blob = TextBlob(tweet.text)
        label = 'Positive'
        if( blob.sentiment.polarity<0 ):
            label = 'Negative'
        writer.writerow( [tweet.text, label] )
        general_polarity += blob.sentiment.polarity
        general_subjectivity += blob.sentiment.subjectivity

    general_polarity /= len(public_tweets)
    general_subjectivity /= len(public_tweets)
    
    general_label = 'Positive'
    if(general_polarity<0):
        general_label = 'Negative'
    writer.writerow( ["General sentiment polarity", general_label] )
