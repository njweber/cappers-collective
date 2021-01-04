import tweepy
import Private
import DB_Methods
import schedule
import time
from datetime import datetime


#Crawls twitter for tweets. Saving to DB when tweet is a betting tweet. Also checks for duplicates.
def start_crawl():
    #Initialize Authentication for Twitter API and Tweepy
    auth = tweepy.OAuthHandler(Private.TWITTER_API_KEY, Private.TWITTER_API_SECRET)
    auth.set_access_token(Private.TWITTER_KEY, Private.TWITTER_SECRET)
    api = tweepy.API(auth)
    
    #Loop over users here and save tweets that are valid data
    users = ["thecheeze222"] #TODO: Pull this from DB later
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

                #TODO: Add duplicate check before saving to DB.
                if(DB_Methods.check_dupe_tweets(id)):
                    DB_Methods.save_all_tweet(date, name, text, url)
                    if(is_user_specific_bet(users[user_num], text)):
                        DB_Methods.save_bet_tweet(date, name, text, url)
            else:
                tweet_num = 0
                flag = True #Not a tweet from today so go to next user  
    return

# Determines if the tweet is a bet tweet depending on user
def is_user_specific_bet(user, text):
    if(user == "thecheeze222"):
        if("🏀" in text or "🏈" in text):
            return True
    return False






#RUN the crawl script automatically
#schedule.every().day.at("12:00").do(start_crawl)

#while True:
   # schedule.run_pending()
   # time.sleep(5)
#END run crawl script automatically

