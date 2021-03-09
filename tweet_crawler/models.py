from django.db import models

# Create your models here.
class tweets_all(models.Model):
    date = models.DateField()
    name = models.CharField(max_length= 50)
    text = models.TextField()
    url = models.CharField(max_length= 250)
    status_id = models.BigIntegerField()
    class Meta:
        db_table = "tweets_all"

class tweets_bets(models.Model):
    date = models.DateField()
    name = models.CharField(max_length= 50)
    text = models.TextField()
    url = models.CharField(max_length= 250)
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

class parsed_data(models.Model):
    capper = models.CharField(max_length= 50)
    league = models.CharField(max_length= 15)
    week = models.IntegerField()
    date = models.DateField()
    bet_type = models.CharField(max_length= 15)
    units = models.IntegerField()
    odds = models.IntegerField()
    result = models.CharField(max_length= 15)
    unit_calc = models.DecimalField(decimal_places=2, max_digits= 10)
    url = models.CharField(max_length= 250)
    raw_text = models.TextField()
    class Meta:
        db_table = "parsed_data"
