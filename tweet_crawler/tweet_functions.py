import tweepy
import time
import Private
import DB_Methods
from dateutil import tz 
from datetime import datetime

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
            tweet = api.user_timeline(users[user_num], count=50)[tweet_num]
            tweet_date = tweet.created_at
            tweet_date = tweet_date.replace(tzinfo=tz.gettz('UTC'))
            tweet_date = str(tweet_date.astimezone(tz.gettz('Eastern Time Zone')))[0 : 10]
            today = str(datetime.today())[0 : 10]
            if(tweet_date == today): #Tweet from today!
                tweet_num = tweet_num + 1
                date = tweet.created_at
                time_date = date.replace(tzinfo=tz.gettz('UTC'))
                time = time_date.astimezone(tz.gettz('Eastern Time Zone')).strftime("%I:%M:%S %p")
                name = tweet.user.screen_name  
                text = tweet.text
                url = "https://twitter.com/" + name + "/statuses/" + str(tweet.id)
                status_id = tweet.id 
                models = DB_Methods.get_bet_models_by_user(users[user_num])
                if(not DB_Methods.check_dupe_tweets(status_id)):
                    DB_Methods.save_all_tweet(date, time, name, text, url, status_id)
                    if(is_user_specific_bet(text, models)):
                        DB_Methods.save_bet_tweet(date, time, name, text, url, status_id)
                        parse_raw_text_bet_data(date, time, name, text, url)
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
def parse_raw_text_bet_data(date, time, name, text, url):
    lines = text.splitlines()   #Splits up raw text into seperate lines
    for line in lines:
        if(len(lines) == 1):    #Only 1 line means that is the bet line
            bet_line = True
        else:                   #More than 1 line so potentially multiple bet lines
            if(len(line) == 0): #Line empty only a return and contains no data
                bet_line = False
            else:               #Line isnt empty. Need to check if it is a bet line or not
                if(True):       #TODO: Check to make sure line is a bet line
                    bet_line = True
                else:
                    bet_line = False
        #---------------------------------
        # Above checks for it line is a bet line
        #---------------------------------
        # Below saves bet data if it is a bet line
        #---------------------------------
        if (bet_line):
            capper = name           #Same
            date = date             #Same
            time = time             #Same   
            url = url               #Same
            week = parse_week(date) #Same

            #These variables will be independent to each bet line
            league = parse_league(text)     #Potentially Different
            bet_type = parse_bet_type(text) #Potentially Different
            units = parse_units()           #Potentially Different
            odds = parse_odds()             #Potentially Different
            unit_calc = parse_unit_calc()   #Potentially Different
            result = parse_result()         #Different
            DB_Methods.save_parsed_bet_data(capper, league, week, date, time, bet_type, units, odds, result, unit_calc, url, text)
    return
    

def parse_league(text):
    if("basketball" in text):
        #either nba or ncaab
        #if the line text contains NBA team name or location is NBA
        #else is a college
        return "NBA"
    if("football" in text):
        #either nfl or ncaaf
        #if the line text contains NFL team name or location is NFL
        #else is a college
        return "NFL"
    if("baseball" in text):
        #only mlb? or do people bet on college baseball?
        return "MLB"
    return "UNKNOWN" #If all else fails

#Parse the week of the year.
def parse_week(date):
    return date.strftime("%V")

#Parse the type of bet
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

#Parse the units bet
def parse_units():
    return 1

#Parse the odds of the bet
def parse_odds():
    return -110

#Parse the results
def parse_result():
    return "-"

#Parse the units gained or lost
def parse_unit_calc():
    return 0.90

#Drop the tables for testing purposes
def drop_tables():
    DB_Methods.drop_tables()