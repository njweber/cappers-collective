from django.db import models

# Create your models here.
class tweets_all(models.Model):
    date = models.DateField()
    name = models.CharField(max_length= 50)
    text = models.TextField()
    url = models.CharField(max_length= 100)
    status_id = models.BigIntegerField()
    class Meta:
        db_table = "tweets_all"

class tweets_bets(models.Model):
    date = models.DateField()
    name = models.CharField(max_length= 50)
    text = models.TextField()
    url = models.CharField(max_length= 100)
    status_id = models.BigIntegerField()
    class Meta:
        db_table = "tweets_bets"

class twitter_users(models.Model):
    name = models.TextField(max_length= 50)
    class Meta:
        db_table = "twitter_users"

class tweet_models(models.Model):
    user = models.CharField(max_length= 50)
    model = models.CharField(max_length= 50)
    class Meta:
        db_table = "tweet_models"