from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(tweets_all)
class tweets_all_admin(admin.ModelAdmin):
    list_display = ['date','time','name','text','url', 'status_id']

@admin.register(tweets_bets)
class tweet_bets_admin(admin.ModelAdmin):
    list_display = ['date','time','name','text','url', 'status_id']

@admin.register(twitter_users)
class twitter_users_admin(admin.ModelAdmin):
    list_display = ['name', 'enabled']

@admin.register(tweet_models)
class tweet_model(admin.ModelAdmin):
    list_display = ['user', 'model']

@admin.register(bet_line_models)
class bet_line_model(admin.ModelAdmin):
    list_display = ['user', 'model']

@admin.register(parsed_data)
class tweet_parsed_data(admin.ModelAdmin):
    list_display = ['capper', 'league', 'week', 'date', 'time', 'bet_type', 'units', 'odds', 'result', 'unit_calc', 'url', 'raw_text']