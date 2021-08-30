from django.db import models
import DB_Methods

# Create your models here.
class tweets_all(models.Model):
    date = models.DateField()
    name = models.CharField(max_length= 50, choices=DB_Methods.get_user_list_names_only())
    text = models.TextField()
    url = models.CharField(max_length= 250)
    status_id = models.BigIntegerField()
    time = models.CharField(max_length= 50)
    class Meta:
        db_table = "tweets_all"

class tweets_bets(models.Model):
    date = models.DateField()
    name = models.CharField(max_length= 50, choices=DB_Methods.get_user_list_names_only())
    text = models.TextField()
    url = models.CharField(max_length= 250)
    status_id = models.BigIntegerField()
    time = models.CharField(max_length= 50)
    class Meta:
        db_table = "tweets_bets"

class twitter_users(models.Model):
    name = models.CharField(max_length= 70)
    enabled = models.BooleanField()
    class Meta:
        db_table = "twitter_users"

class tweet_models(models.Model):
    user = models.CharField(max_length= 50, choices=DB_Methods.get_user_list_names_only())
    model = models.CharField(max_length= 50)
    class Meta:
        db_table = "tweet_models"

class win_models(models.Model):
    user = models.CharField(max_length= 50, choices=DB_Methods.get_user_list_names_only())
    model = models.CharField(max_length= 50)
    class Meta:
        db_table = "win_models"

class loss_models(models.Model):
    user = models.CharField(max_length= 50, choices=DB_Methods.get_user_list_names_only())
    model = models.CharField(max_length= 50)
    class Meta:
        db_table = "loss_models"

class bet_line_models(models.Model):
    user = models.CharField(max_length= 50, choices=DB_Methods.get_user_list_names_only())
    model = models.CharField(max_length= 50)
    class Meta:
        db_table = "bet_line_models"

class mlb_models(models.Model):
    text = models.CharField(max_length= 50)
    class Meta:
        db_table = "mlb_models"

class nba_models(models.Model):
    text = models.CharField(max_length= 50)
    class Meta:
        db_table = "nba_models"

class ncaab_models(models.Model):
    text = models.CharField(max_length= 50)
    class Meta:
        db_table = "ncaab_models"

class ncaaf_models(models.Model):
    text = models.CharField(max_length= 50)
    class Meta:
        db_table = "ncaaf_models"

class nfl_models(models.Model):
    text = models.CharField(max_length= 50)
    class Meta:
        db_table = "nfl_models"

class nhl_models(models.Model):
    text = models.CharField(max_length= 50)
    class Meta:
        db_table = "nhl_models"

class parsed_data(models.Model):
    capper = models.CharField(max_length= 50, choices=DB_Methods.get_user_list_names_only())
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
    time = models.CharField(max_length= 50)
    class Meta:
        db_table = "parsed_data"
