import tweepy
import Private
import DB_Methods

def start_crawl():
    #Initialize Authentication for Twitter API and Tweepy
    auth = tweepy.OAuthHandler(Private.TWITTER_API_KEY, Private.TWITTER_API_SECRET)
    auth.set_access_token(Private.TWITTER_KEY, Private.TWITTER_SECRET)
    api = tweepy.API(auth)

    #Will need to loop over users here and save tweets that are valid data
    public_tweet = api.user_timeline("thecheeze222")[1]
    text = public_tweet.text
    date = public_tweet.created_at
    name = public_tweet.user.screen_name  
    url = public_tweet.id 
    DB_Methods.save_tweet(date, name, text, url)
    return