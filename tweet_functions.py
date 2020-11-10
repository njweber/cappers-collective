import tweepy
import Private
import DB_Methods

def start_crawl():
    #Initialize Authentication for Twitter API and Tweepy
    auth = tweepy.OAuthHandler(Private.TWITTER_API_KEY, Private.TWITTER_API_SECRET)
    auth.set_access_token(Private.TWITTER_KEY, Private.TWITTER_SECRET)
    api = tweepy.API(auth)

    #Will need to loop over users here and save tweets that are valid data
    tweet = api.user_timeline("thecheeze222")[1]
    date = tweet.created_at
    name = tweet.user.screen_name  
    text = tweet.text
    url = "https://twitter.com/" + name + "/statuses/" + str(tweet.id) 
    DB_Methods.save_tweet(date, name, text, url)
    return
