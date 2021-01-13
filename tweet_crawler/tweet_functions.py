import tweepy
import Private
import DB_Methods
import time
from datetime import datetime  

#TODO: Crawl site daily! Possibly use celery.

#Crawls twitter for tweets. Saving to DB when tweet is a betting tweet. Also checks for duplicates.
def start_crawl():
    print("Crawling!")
    #Initialize Authentication for Twitter API and Tweepy
    auth = tweepy.OAuthHandler(Private.TWITTER_API_KEY, Private.TWITTER_API_SECRET)
    auth.set_access_token(Private.TWITTER_KEY, Private.TWITTER_SECRET)
    api = tweepy.API(auth)
    
    #Loop over users here and save tweets that are valid data
    
    users = DB_Methods.get_user_list() #Pull list of users from the database
    for user_num in range(len(users)):
        flag = False
        tweet_num = 0
        while (flag == False):
            tweet = api.user_timeline(users[user_num])[tweet_num]
            tweet_date = str(tweet.created_at)[0 : 10]
            today = str(datetime.today())[0 : 10]
            if(tweet_date == today): #Tweet from today!
                tweet_num = tweet_num + 1
                date = tweet.created_at
                name = tweet.user.screen_name  
                text = tweet.text
                url = "https://twitter.com/" + name + "/statuses/" + str(tweet.id)
                status_id = tweet.id 

                if(not DB_Methods.check_dupe_tweets(status_id)):
                    DB_Methods.save_all_tweet(date, name, text, url, status_id)
                    if(is_user_specific_bet(users[user_num], text)):
                        DB_Methods.save_bet_tweet(date, name, text, url, status_id)
            else:
                tweet_num = 0
                flag = True #Not a tweet from today so go to next user  
    return

# Determines if the tweet is a bet tweet depending on user
def is_user_specific_bet(user, text):
    if(user == "thecheeze222"):
        if("🏀" in text or "🏈" in text):
            return True
    if(user == ""):
        return True
    return False