import psycopg2
import pandas as pd
import os
from sqlite3 import Error

connect = psycopg2.connect(
    host="ec2-54-82-208-124.compute-1.amazonaws.com",
    database="d1acr589hq47f4",
    user="jlkghpyceaceaj",
    password="5d3ff149d535057886dfd52ac85888eb2f28f2ba34c5f36b46429d99720f7f36")

cursor = connect.cursor()

def save_bet_tweet(date, time, name, text, url, status_id):
    cursor.execute("INSERT INTO tweets_bets (date, name, text, url, status_id, time) VALUES (%s, %s, %s, %s, %s, %s)", (date, name, text, url, status_id, time))
    connect.commit()
    return 1

def save_all_tweet(date, time, name, text, url, status_id):
    cursor.execute("INSERT INTO tweets_all (date, name, text, url, status_id, time) VALUES (%s, %s, %s, %s, %s, %s)", (date, name, text, url, status_id, time))
    connect.commit()
    return 1

def save_parsed_bet_data(capper, league, week, date, time, bet_type, units, odds, result, unit_calc, url, raw_text):
    cursor.execute("INSERT INTO parsed_data (capper, league, week, date, bet_type, units, odds, result, unit_calc, url, raw_text, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (capper, league, week, date, bet_type, units, odds, result, unit_calc, url, raw_text, time))
    connect.commit()
    return 1


def check_dupe_tweets(id):
    cursor.execute("SELECT * FROM tweets_all")
    for row in cursor:
        if(row[5] == id):
            return True
    return False

def get_user_list():
    cursor.execute("SELECT * FROM twitter_users")
    users = []
    for row in cursor:
        users.append(row)
    return users 

def get_user_list_names_only():
    cursor.execute("SELECT * FROM twitter_users")
    users = ()
    for row in cursor:
        users += ((str(row[1]), str(row[1])),)
    return users
    
def get_bet_models_by_user(user):
    cursor.execute("SELECT * FROM tweet_models")
    models = []
    for row in cursor:
        if (row[1] == user):
            models.append(row[2])
    return models 

def get_win_models_by_user(user):
    cursor.execute("SELECT * FROM win_models")
    models = []
    for row in cursor:
        if (row[1] == user):
            models.append(row[2])
    return models 

def get_loss_models_by_user(user):
    cursor.execute("SELECT * FROM loss_models")
    models = []
    for row in cursor:
        if (row[1] == user):
            models.append(row[2])
    return models 

def get_bet_line_models_by_user(user):
    cursor.execute("SELECT * FROM bet_line_models")
    models = []
    for row in cursor:
        if (row[1] == user):
            models.append(row[2])
    return models 

## START LEAGUE DATABASE CHECKS

def doesTextContainMLB(text):
    cursor.execute("SELECT * FROM mlb_models")
    for row in cursor:
        if(row[1].lower() in text.lower()):
            return True
    return False

def doesTextContainNBA(text):
    cursor.execute("SELECT * FROM nba_models")
    for row in cursor:
        if(row[1].lower() in text.lower()):
            return True
    return False

def doesTextContainNCAAB(text):
    cursor.execute("SELECT * FROM ncaab_models")
    for row in cursor:
        if(row[1].lower() in text.lower()):
            return True
    return False

def doesTextContainNHL(text):
    cursor.execute("SELECT * FROM nhl_models")
    for row in cursor:
        if(row[1].lower() in text.lower()):
            return True
    return False

def doesTextContainNFL(text):
    cursor.execute("SELECT * FROM nfl_models")
    for row in cursor:
        if(row[1].lower() in text.lower()):
            return True
    return False

def doesTextContainNCAAF(text):
    cursor.execute("SELECT * FROM ncaaf_models")
    for row in cursor:
        if(row[1].lower() in text.lower()):
            return True
    return False

## END LEAGUE DATABASE CHECKS

#This will be deleted eventually!
def drop_tables():
    cursor.execute("DELETE FROM tweets_all")
    cursor.execute("DELETE FROM tweets_bets")
    cursor.execute("DELETE FROM parsed_data")
    connect.commit()
    return 1

def export_to_excel():
    week = 18 #Edit this to week we want to archive
    query = "SELECT * FROM parsed_data WHERE week = " + str(week)
    df = pd.read_sql(query, connect)
    path = 'cappers_collective_parsed_data_week_' + str(week) + '.xlsx'
    df.to_excel(path)
    return 1

    #Once we archive we want to clean out the DB of archived data
    #cursor.execute("DELETE FROM parsed_data WHERE week = 33")
    #connect.commit()

