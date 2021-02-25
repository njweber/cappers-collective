import tweepy
import time
import Private
import DB_Methods
from datetime import datetime  

#Crawls twitter for tweets. Saving to DB when tweet is a betting tweet. Also checks for duplicates.
def start_crawl():
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
                models = DB_Methods.get_bet_models_by_user(users[user_num])
                if(not DB_Methods.check_dupe_tweets(status_id)):
                    DB_Methods.save_all_tweet(date, name, text, url, status_id)
                    if(is_user_specific_bet(text, models)):
                        DB_Methods.save_bet_tweet(date, name, text, url, status_id)
                        parse_raw_text_bet_data(date, name, text, url)
            else:
                tweet_num = 0
                flag = True #Not a tweet from today so go to next user  
    return

# Determines if the tweet is a bet tweet depending on user
def is_user_specific_bet(text, models):
    for model in models:
        if(model in text):
            return True
    return False

# Parse Raw Text Bet Data 
#TODO: Parse bet data into individual fields
def parse_raw_text_bet_data(date, name, text, url):
    capper = name
    date = date 
    url = url
    league = parse_league()
    week = parse_week(date)
    bet_type = parse_bet_type(text)
    units = parse_units()
    odds = parse_odds()
    result = parse_result()
    unit_calc = parse_unit_calc()
    return #DB_Methods.save_parsed_bet_data(capper, league, week, date, bet_type, units, odds, result, unit_calc, url)
    

def parse_league():
    return ""

def parse_week(date):
    return date.strftime("%V")

def parse_bet_type(text):
    split = text.split(' ')
    print(split)
    
    if():
        #Spread bet
        return "SP"
    if():
        #Over under bet  
        return "OU"  
    if():
        #Money line bet
        return "ML"
    if(): 
        #Player prop bet
        return "PR"
    if():
        #Teaser bet
        return "TS"
    if():
        #Parlay bet
        return "PARLAY"

def parse_units():
    return ""

def parse_odds():
    return ""

def parse_result():
    return ""

def parse_unit_calc():
    return ""