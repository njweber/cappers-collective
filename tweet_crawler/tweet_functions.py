# Finish Unit Parsing
import psycopg2
import emoji
import tweepy
import re
import os
import Private
import DB_Methods
from dateutil import tz 
from datetime import datetime
from django.shortcuts import render

#TODO: Add reporting to crawl and send email with report details.
#TODO: Look into adding junk lines to the bet lines. Would need to create an array of junk lines and add to end/start of bet line.
#TODO: Odds with greater than 4 digits are not working.

# Potential Format
# Anything separated by spaces or commas would work best.
#
##WITH HEADER##
# LEAGUE - UNITS
# Info/Team, Bet Type, Odds, Result
# Info/Team, Bet Type, Odds, Result
# Info/Team, Bet Type, Odds, Result
#
##WITHOUT HEADER##
# League, Units, Bet Type, Odds, Result 
#
# A hashtag could be nice to be able to know which tweets are bet tweets

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

    #Reported data list
    report_list = []
    for i in range(len(users)):
        report_list.append([])

    report_count = 0
    for user_num in range(len(users)):
        flag = False
        tweet_num = 0
        bet_num = 0
        report_list[report_count].append(users[user_num])
        while (flag == False):
            try:
                tweet = api.user_timeline(users[user_num], count=50, tweet_mode="extended")[tweet_num]
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
                    text = emoji.demojize(tweet.full_text, delimiters=("", ""))
                    url = "https://twitter.com/" + name + "/statuses/" + str(tweet.id)
                    status_id = tweet.id 
                    models = DB_Methods.get_bet_models_by_user(users[user_num]) + DB_Methods.get_bet_models_by_user("ALL_USERS")
                    bet_line_models = DB_Methods.get_bet_line_models_by_user(users[user_num]) + DB_Methods.get_bet_line_models_by_user("ALL_USERS")
                    win_models = DB_Methods.get_win_models_by_user(users[user_num]) + DB_Methods.get_win_models_by_user("ALL_USERS")
                    loss_models = DB_Methods.get_loss_models_by_user(users[user_num]) + DB_Methods.get_loss_models_by_user("ALL_USERS")
                    if(not DB_Methods.check_dupe_tweets(status_id)):
                        DB_Methods.save_all_tweet(date, time, name, text, url, status_id)
                        if(is_user_specific_bet(text, models)):
                            bet_num = bet_num + 1
                            DB_Methods.save_bet_tweet(date, time, name, text, url, status_id)
                            parse_raw_text_bet_data(date, time, name, text, url, bet_line_models, win_models, loss_models)
                else:
                    tweet_num = 0
                    flag = True #Not a tweet from today so go to next user  
                    #report_list[report_count].append(tweet_num)
                    #report_list[report_count].append(bet_num)
                    report_count = report_count + 1
            except:
                tweet_num = 0
                flag = True #Not a tweet from today so go to next user  
                #report_list[report_count].append(tweet_num)
                #report_list[report_count].append(bet_num)
                report_count = report_count + 1
    #create_report(report_list)
    return report_list

# Determines if the tweet is a bet tweet depending on user
def is_user_specific_bet(text, models):
    for model in models:
        if(model in text):
            return True
    return False

#TODO: ...
# Reports the information found during a crawl

# Parse Raw Text Bet Data 
def parse_raw_text_bet_data(date, time, name, text, url, bet_line_models, win_models, loss_models):
    lines = text.splitlines()       #Splits up raw text into seperate lines
    league_headers = check_league_header(lines)
    units_headers = check_units_header(lines)
    line_number = -1
    for line in lines:
        line_number += 1
        if(len(lines) == 1):        #Only 1 line means that is the bet line
            bet_line = True
        else:                       #More than 1 line so potentially multiple bet lines
            if(len(line) == 0):     #Line empty only a return and contains no data
                bet_line = False
            else:                   #Line isnt empty. Need to check if it is a bet line or not
                bet_line = False
                for model in bet_line_models:
                    if(model in line):
                        bet_line = True

        # Above checks for if line is a bet line
        #---------------------------------
        # Below saves bet data if it is a bet line
        #---------------------------------
        
        if (bet_line):
            if(containsNumbers(line)):
                capper = name           #Same
                date = date             #Same
                time = time             #Same   
                url = url               #Same
                week = parse_week(date) #Same

                #These variables will be independent to each bet line
                league = parse_league(line, league_headers, line_number)
                bet_type = parse_bet_type(line)
                units = parse_units(line, units_headers, line_number)
                odds = parse_odds(line)
                result = parse_result(line, win_models, loss_models)          
                unit_calc = parse_unit_calc(odds, units, result)
                line = re.sub(r'http\S+', '', line)
                DB_Methods.save_parsed_bet_data(capper, league, week, date, time, bet_type, units, odds, result, unit_calc, url, line)
    return

def check_league_header(lines):
    league_list = ["NFL", "NBA", "NHL", "MLB", "NCAAB", "NCAAF"]
    line_number = 0
    league_line_data = {}
    current_league = ""
    for line in lines:
        line_number+=1
        for league in league_list:
            line_temp = line.lower()
            league_temp = league.lower()
            if league_temp in line_temp:
                current_league = league_temp
        league_line_data[line_number] = current_league.upper()
    return league_line_data
    
def check_units_header(lines):
    line_number = 0
    units_line_data = {}
    current_units = 0
    for line in lines:
        line_number+=1
        #If line contains units
            #current_units = found_units
        units_line_data[line_number] = current_units
    return units_line_data

def parse_league(text, league_headers, line_number):
    if(DB_Methods.doesTextContainNBA(text)):
        return "NBA"
    if(DB_Methods.doesTextContainNCAAB(text)):
        return "NCAAB"
    if(DB_Methods.doesTextContainNFL(text)):
        return "NFL"
    if(DB_Methods.doesTextContainNCAAF(text)):
        return "NCAAF"
    if(DB_Methods.doesTextContainMLB(text)):
        return "MLB"
    if(DB_Methods.doesTextContainNHL(text)):
        return "NHL"
    return league_headers[line_number]

#Parse the week of the year.
def parse_week(date):
    return date.strftime("%V")

#Parse the type of bet
def parse_bet_type(text):
    split = text.split(' ')
    for snip in split:
        #Spread bet
        temp_snip = snip.replace("-", "")
        temp_snip = temp_snip.replace("+", "")
        temp_snip = temp_snip.replace(".", "")
        if(temp_snip.isdecimal() and int(temp_snip) < 100):
            return "SP"  

        #Over under bet
        if( len(snip) > 1 ):    
            if((snip[0] == "U" or snip[0] == "O") and snip[1:].isnumeric()):
                return "OU"  
            if(snip.lower() == "over" or snip.lower() == "under"):
                return "OU"
        
    #TODO: Parse player prop bets
    if(): 
        #Player prop bet
        return "PR"
    #TODO: Parse teaser bets
    if():
        #Teaser bet
        return "TS"
    #TODO: Parse parley bets
    if():
        #Parlay bet
        return "PARLAY"
        
    #Money line bet if nothing else
    return "ML"

#Parse the units bet
def parse_units(line, units_headers, line_number):
    try:
        split = line.split(' ')
        for snip in split:
            temp_snip = snip.replace("(", "")
            temp_snip = temp_snip.replace(")", "")
            temp_snip = temp_snip.replace("+", "")
            temp_snip = temp_snip.replace("-", "")
            if(temp_snip[-1].lower() == "u"):
                temp = temp_snip[:-1].replace('.','',1)
                if(temp.isnumeric()):
                    return temp_snip[:-1]
        return 1 #units_headers[line_number]
    except:
        print("There was a problem parsing units")
        return 1
    

#Parse the odds of the bet
def parse_odds(text):
    split = text.split('+')
    for snip in split:
        if(snip[0:3].isnumeric()):
            if(int(snip[0:3]) > 99 or int(snip[0:3]) < -99):
                return "+" + snip[0:3]
    split = text.split('-')
    for snip in split:
        if(snip[0:3].isnumeric()):
            if(int(snip[0:3]) > 99 or int(snip[0:3]) < -99):
                return "-" + snip[0:3]
    return -110

#Parse the results
def parse_result(text, win_models, loss_models):
    for model in win_models:
        if(model in text):
            return "W"
    for model in loss_models:
        if(model in text):
            return "L"
    return "-"

#Parse the units gained or lost
def parse_unit_calc(odds, units, result):
    if(result == "L"):
        return "-" + str(units)
    if(int(odds) < 0):
        temp = -100/int(odds)
        calc =  temp * float(units)
    else:
        calc = float(int(odds)/100) * float(units) 
    return "+" + str(calc)

def containsNumbers(value):
    for character in value:
        if character.isdigit():
            return True
    return False

#TODO: Remove this eventually
#Drop the tables for testing purposes
def drop_tables():
    #DB_Methods.drop_tables()
    DB_Methods.export_to_excel()