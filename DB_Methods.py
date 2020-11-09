import psycopg2

connect = psycopg2.connect(
    host="ec2-54-82-208-124.compute-1.amazonaws.com",
    database="d1acr589hq47f4",
    user="jlkghpyceaceaj",
    password="5d3ff149d535057886dfd52ac85888eb2f28f2ba34c5f36b46429d99720f7f36")

cursor = connect.cursor()

def save_tweet(user, date, text, url):
    #cursor.execute("INSERT INTO tweet (user, date, text, url) VALUES ('testuser',%s, %s, %s)", (date, text, url))
    print(cursor.execute("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'tweet'"))
    connect.commit()
    return "Tweet Saved"
