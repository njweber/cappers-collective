import psycopg2

connect = psycopg2.connect(
    host="ec2-54-82-208-124.compute-1.amazonaws.com",
    database="d1acr589hq47f4",
    user="jlkghpyceaceaj",
    password="5d3ff149d535057886dfd52ac85888eb2f28f2ba34c5f36b46429d99720f7f36")

cursor = connect.cursor()

def save_bet_tweet(date, name, text, url):
    cursor.execute("INSERT INTO tweets_bets (date, name, text, url) VALUES (%s, %s, %s, %s)", (date, name, text, url))
    connect.commit()
    return 1

def save_all_tweet(date, name, text, url):
    cursor.execute("INSERT INTO tweets_all (date, name, text, url) VALUES (%s, %s, %s, %s)", (date, name, text, url))
    connect.commit()
    return 1

def check_dupe_tweets(id):
    
    if(cursor.execute("SELECT id FROM tweets_all WHERE id = 41")):
        print("YES")
        #return True
    return False