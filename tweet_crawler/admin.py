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

@admin.register(win_models)
class win_models(admin.ModelAdmin):
    list_display = ['user', 'model']

@admin.register(loss_models)
class loss_model(admin.ModelAdmin):
    list_display = ['user', 'model']

@admin.register(mlb_models)
class mlb_model(admin.ModelAdmin):
    list_display = ['text']

@admin.register(nba_models)
class nba_model(admin.ModelAdmin):
    list_display = ['text']

@admin.register(ncaab_models)
class ncaab_model(admin.ModelAdmin):
    list_display = ['text']

@admin.register(ncaaf_models)
class ncaaf_model(admin.ModelAdmin):
    list_display = ['text']

@admin.register(nfl_models)
class nfl_model(admin.ModelAdmin):
    list_display = ['text']

@admin.register(nhl_models)
class nhl_model(admin.ModelAdmin):
    list_display = ['text']

@admin.register(parsed_data)
class tweet_parsed_data(admin.ModelAdmin):
    list_display = ['capper', 'league', 'week', 'date', 'time', 'bet_type', 'units', 'odds', 'result', 'unit_calc', 'url', 'raw_text']
    search_fields = ['capper', 'league', 'week']