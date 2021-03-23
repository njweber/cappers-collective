import tweepy
import time
import Private
import DB_Methods
from dateutil import tz
from datetime import datetime

#DONE: Fix not all users pulled
#DONE: Allow toggling users data pull
#DONE: Fix run daily
#DONE: Clear tables for testing
#DONE: Fix time thingy was pulling UTC?? WHYYY
#TODO: Split single/mult bet tweet into seperate items
#TODO: Add times of tweet not just the date
#TODO: Continue league and bet type parsing
#TODO: Look into excel archiving 


#Crawls twitter for tweets. Saving to DB when tweet is a betting tweet. Also checks for duplicates.
def start_crawl():
    #Initialize Authentication for Twitter API and Tweepy
    auth = tweepy.OAuthHandler(Private.TWITTER_API_KEY, Private.TWITTER_API_SECRET)
    auth.set_access_token(Private.TWITTER_KEY, Private.TWITTER_SECRET)
    api = tweepy.API(auth)
    
    #Loop over users here and save tweets that are valid data
    users = []
    users_all = DB_Methods.get_user_list() #Pull list of users from the database
    for u in users_all:
        if(u[2] == True):
            users.append(u[1])
    for user_num in range(len(users)):
        flag = False
        tweet_num = 0
        while (flag == False):
            tweet = api.user_timeline(users[user_num])[tweet_num]
            tweet_date = tweet.created_at
            tweet_date = tweet_date.replace(tzinfo=tz.gettz('UTC'))
            tweet_date = str(tweet_date.astimezone(tz.gettz('Eastern Time Zone')))[0 : 10]
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
    league = parse_league(text)
    week = parse_week(date)
    bet_type = parse_bet_type(text)
    units = parse_units()
    odds = parse_odds()
    result = parse_result()
    unit_calc = parse_unit_calc()
    return DB_Methods.save_parsed_bet_data(capper, league, week, date, bet_type, units, odds, result, unit_calc, url, text)
    

def parse_league(text):
    if("basketball" in text):
        #either nba or ncaab
        return "NBA"
    if("football" in text):
        #either nfl or ncaaf
        return "NFL"
    if("baseball" in text):
        #only mlb? or do people bet on college baseball?
        return "MLB"
    return "UNKNOWN"

#DONE
def parse_week(date):
    return date.strftime("%V")

def parse_bet_type(text):
    split = text.split(' ')
    for snips in split:
        #print(snips)
        try: #Spread bet
            flag = int(snips) < 100 and int(snips) > -100 
            #print(flag)
        except:
            break #Not a valid data type
        if (flag is True):
            print("Spread!")
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
    return "UNKNOWN"

def parse_units():
    return 1

def parse_odds():
    return -110

def parse_result():
    return "-"

def parse_unit_calc():
    return 0.90

def drop_tables():
    DB_Methods.drop_tables()