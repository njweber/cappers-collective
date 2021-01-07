from django.contrib import admin

# Register your models here.
from .models import tweets_all
from .models import tweets_bets

@admin.register(tweets_all)
class tweets_all_admin(admin.ModelAdmin):
    list_display = ['id','date','name','text','url']

@admin.register(tweets_bets)
class tweet_bets_admin(admin.ModelAdmin):
    list_display = ['id','date','name','text','url']

